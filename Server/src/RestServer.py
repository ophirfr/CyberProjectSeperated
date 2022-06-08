import pickle
import cv2
import face_recognition
from flask import Flask, request, make_response
from flask_restful import Api, Resource
from flask import jsonify, redirect
import os
from werkzeug.utils import secure_filename
from DataBaseDriver import DataBase
import shutil
from functools import wraps
import jwt
import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from ServerConfig import ServerSettings

SrvSettings = ServerSettings()

app = Flask(__name__)
api = Api(app)
dataBase = DataBase()


# input- fileName
# Checks if the fuke is allowed
def allowed_file(fileName):
    return '.' in fileName and fileName.rsplit('.', 1)[1].lower() in SrvSettings.GetAllowedMediaExt()

#Input- user id
#Output- directory path
# Creates a directory and name it after the "id"
def makeDirectory(id):
    directory = str(id)
    parent_dir = SrvSettings.GetUploadPicProtoPath()
    path = os.path.join(parent_dir, directory)
    if (os.path.isdir(path) == False):
        os.makedirs(path)
    return path

#Input- user id
#return the path to the prototype  picture dir
def GetDirByID(id):
    directory = str(id)
    parent_dir = SrvSettings.GetUploadPicProtoPath()
    path = os.path.join(parent_dir, directory)
    return path


#file- jpg file in dir id
#dir-saves the face model into a dir "id"
def CreateFaceModel(fileName,dir):
    jpg_path=dir+"/"+fileName
    img=cv2.imread(jpg_path)
    rgbImg=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    imgEncoding=face_recognition.face_encodings(rgbImg)[0]
    with open (dir+"/model.dat",'wb') as f:
        pickle.dump(imgEncoding,f)



#id- prototype image of an id in data base
#PathPIc- image to compare to prototype
def CompareFaceModel(id,pathPic):
    path=GetDirByID(id)+"/model.dat"
    try:
        with open(path,'rb') as f:
            imgEncoding=pickle.load(f)
    except EnvironmentError:  # parent of IOError, OSError *and* WindowsError where available
        return False

    img = cv2.imread(pathPic)
    rgbImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    imgEncoding2 = face_recognition.face_encodings(rgbImg)[0]
    result=face_recognition.compare_faces([imgEncoding],imgEncoding2)
    return result

# decorator function that check the token is valid only
# on operations that involve write/delete
# if the token exits and correct the original function is called
def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']
        if not token:
            return 'A valid token is missing',400
        try:
            data = jwt.decode(token,SrvSettings.GetSecretKey(), algorithms=["HS256"])
            #current_user = data['RestServer']
        except jwt.DecodeError:
            return 'token is invalid',400
        except jwt.ExpiredSignatureError:
            return 'Token expired',401
            
        return f(*args, **kwargs)

    return decorator

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#
class APIDBServerId(Resource):
    method_decorators = {'post':[token_required],'delete':[token_required]}


    def get(self, id):
        # return dict
        res = dataBase.getById(id)
        if len(res) == 0 or res == 0:
            return "User not found", 400
        return res, 200


    def delete(self, id):
        if (dataBase.delete(id) != 0):
            return id, 200
        return 0, 400


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

class APIDBServer(Resource):
    # מה שיקרה כאשר פקודת get נשלחת
    method_decorators = {'post':[token_required],'delete':[token_required]}
    def get(self):
        data = dataBase.getAll()
        if (data != 0):
            return data, 200
        return "user not found ", 400

    # Provide id in JSON body
    def addUser(self):
        if request.is_json:
            data = request.get_json()
            id1 = data["user_id"]
            name = data["name"]
            per = data["per"]
            if dataBase.insert_values(id1, name, per) != 0:
                return data, 200
        return "can not add user", 400

    def post(self):
        res, status = self.addUser()
        if status == 200:
            return res, status
        return res, status


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


class APIFileHandler(Resource):
    # מה שיקרה כאשר פקודת get נשלחת
    method_decorators = {'post':[token_required],'delete':[token_required]}


# Input- user id
# checks if the file name exits in the HTTP headers if so creats a dir by the name of"id"
# saves the pic in the dir , creates a face model and saves in the same dir
    def upload_file(self,  id):
        # check if the post request has the file part
        if 'file' not in request.files:
            return "No file part in the request", 400
        file = request.files['file']
        if file.filename == '':
            return "No file selected for uploading", 400
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            #filename=file.filename
            path = makeDirectory( id)
            file.save(os.path.join(path, filename))
            CreateFaceModel(filename,path)
            return "File successfully uploaded", 201
        else:
            return "Allowed file types are jpg, jpeg", 400

    def post(self,  id):
        return self.upload_file(id)



    def delete (self, id):
        folderPath=GetDirByID(id)
        shutil.rmtree(folderPath)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


class APIFaceId(Resource):

#Uplodes the picture to tmp dir in the server side ,and comperes between the exsiting model to the new model of the picture
    def getFileAndFaceCompere (self, id, fileName):
        # check if the post request has the file part
        if 'file' not in request.files:
            return "No file part in the request", 400
        file = request.files['file']
        if file.filename == '':
            return "No file selected for uploading", 400
        if file and allowed_file(file.filename):
            #filename = secure_filename(file.filename)
            #filename = file.filename
            path=os.path.join(SrvSettings.GetUploadPicTmpPath(), fileName)
            file.save(path)

            ret = CompareFaceModel(id,path)
            if ret[0]== True:
                return "Face: PASS", 200
            else:
                return "Face: FAIL", 400

    def post(self, id, jpg_file):
        return self.getFileAndFaceCompere(id,jpg_file)



#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



class APILogIn(Resource):

#בודק אם הסיסמא שקיבל והסיסמא שנשמרה בקובץ זהות בעזרת פונקציית  hash , ובודק את השם משתמש
    def CheckLogIn(self):
        auth = request.authorization
        if not auth or not auth.username or not auth.password:
            return make_response('could not verify', 401, {'Authentication': 'login required"'})
        #global AdminPass
        if check_password_hash(SrvSettings.GetPassword(), auth.password) and SrvSettings.GetAdminName() == auth.username:
            token = jwt.encode({'RestServer': 'Ophir', 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=10)},
                               SrvSettings.GetSecretKey(), "HS256")
            return jsonify({'token': token})

        return make_response('could not verify', 401, {'Authentication': '"login required"'})


    def post(self):
        return self.CheckLogIn()


api.add_resource(APIDBServerId,"/user/<int:id>")
api.add_resource(APIDBServer, "/user")
api.add_resource(APIFileHandler, "/file_op/<int:id>")
api.add_resource(APIFaceId, "/compare/<int:id>/<string:jpg_file>")
api.add_resource(APILogIn, "/login")



if __name__ == "__main__":
    SrvSettings.ReadSetting()
    app.run(debug=True, host="0.0.0.0",port=SrvSettings.GetServerPort(),ssl_context='adhoc')

   # x=CompareFaceModel(676767, r"C:\Users\ophir\PycharmProjects\facedetectionexample\pictures\pics\676767\roy.jpeg")
    #print(x)
    #x = CompareFaceModel(676767, r"C:\Users\ophir\PycharmProjects\facedetectionexample\pictures\ophir.jpeg")
    #print(x)
