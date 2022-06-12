
import json

class ServerSettings():
    def __init__(self):
        self.UploadFolderPicProto = r'..//pic_proto'
        self.UploadFolderPicTmp = r'..//pic_tmp_server'
        self.AllowedExt =  set(['jpg', 'jpeg'])
        self.SeverPort = 5000
        self.AdminName = ""
        self.AdminPass = ""
        self.SecretKey = "1100"

# פותח קובץ קורא ממנו את הנתונים ומכניס למשתני המחלקה
    def ReadSetting(self):
        # Opening JSON file
        try:
            with open('../setting_server/Setting.json', 'r') as openfile:
                json_object = json.load(openfile)
        except FileNotFoundError:
            print('can not find the file')
            return
        self.SetAdminName(json_object["user_name"])
        self.SetPass(json_object["password"])
        self.SetServerPort(json_object["port"])

    def SetAdminName(self,name):
        self.AdminName = name

    def SetPass(self,pwd):
        self.AdminPass = pwd

    def SetServerPort(self,port):
        self.SeverPort = port

    def GetServerPort(self):
        return self.SeverPort

    def GetAdminName(self):
        return self.AdminName

    def GetPassword(self):
        return self.AdminPass

    def GetUploadPicProtoPath(self):
        return self.UploadFolderPicProto

    def GetUploadPicTmpPath(self):
        return self.UploadFolderPicTmp


    def GetSecretKey(self):
        return self.SecretKey


    def GetAllowedMediaExt(self):
        return self.AllowedExt

