import requests


class RestAPI:

#-----------------------------------------------
#
#
#-----------------------------------------------
    def GetDataAll(self, api_url):
        URL = api_url + "/user"
        response = requests.get(URL, verify=False)
        return response.json(), response.status_code

#-----------------------------------------------
#param - Id : המספר המזהה של המשתמש שעליו רוצים לקבל את המידע , api_url- url שבו רץ הסרבר
#return - פרטי המשתמש , status_code
#-----------------------------------------------

    def GetData(self, api_url, Id):
        URL = api_url + "/user/" + str(Id)
        try:
            response = requests.get(URL, verify=False)
            return response.json(), response.status_code
        except (requests.ConnectionError, requests.Timeout):
            return "No internet connection.", 500

#-----------------------------------------------
#param - Id : המספר המזהה של המשתמש שאותו רוצים למחוק  , api_url- url שבו רץ הסרבר
#token-
#return - פרטי המשתמש , status_code
#-----------------------------------------------

    def DeleteUserId(self, api_url, id,token):
        URL = api_url + "/user/" + str(id)
        MyHeaders = {"x-access-tokens": token}
        response = requests.delete(URL,headers=MyHeaders, verify=False)
        return response.json(), response.status_code

#-----------------------------------------------
#param - Id : הפרטיים של  המשתמש שאותו רוצים להוסיף  , api_url- url שבו רץ הסרבר
#token-
#return - פרטי המשתמש , status_code
#-----------------------------------------------

    def AddUser(self, api_url, user,token):
        URL = api_url + "/user"
        MyHeaders = {"x-access-tokens": token}
        response = requests.post(URL, json=user,headers=MyHeaders, verify=False)
        return response.json(), response.status_code


#-----------------------------------------------
#
#
#-----------------------------------------------
    def UploadPic(self, api_url, id, path,token):
        URL = api_url + "/file_op" + "/" + str(id)
        try:
            f = open(path, 'rb')
        except IOError:
            return "Cant find JPEG file", 404
        files = {'file': f}
        MyHeaders = {"x-access-tokens": token}
        response = requests.post(URL, files=files ,headers=MyHeaders, verify=False)
        return response.json(), response.status_code

#-----------------------------------------------
#
#
#-----------------------------------------------
    def CompareImages(self,api_url,id, fileName):
        URL = api_url + "/compare" + "/" + str(id) + "/" +"tmp.jpg"
        try:
            f = open(fileName, 'rb')
        except IOError:
            return "Cant find file", 404
        files = {'file': f}
        response = requests.post(URL, files=files, verify=False)
        return response.json(), response.status_code
      
#-----------------------------------------------
#
#
#-----------------------------------------------
    def DeleteFolderByID(self,api_url, id, token ):
        URL = api_url + "/" + "file_op" + "/" + str(id)
        MyHeaders = {"x-access-tokens": token}
        response = requests.delete(URL, headers=MyHeaders, verify=False)
        return response, response.status_code
#-----------------------------------------------
#
#
#-----------------------------------------------
    def LogIn(self,api_url, password, userName):
        URL = api_url + "/" + "login"
        try:
            response = requests.post(URL, data={}, auth=(userName, password),verify=False)  # do not check certificate (חתימה עצמאית)
            return response, response.status_code
        except (requests.ConnectionError, requests.Timeout) :
            return "No internet connection.", 500



''' 
#update the old data with new data
    def put(self, api_url, id, newData ):
        URL =api_url + "/" + str(id)
        response = requests.get(URL)
        response = requests.put(URL , json=newData)
        response.json()
        return response.status_code

'''

# בדיקות של ה RestAPi

def main():
    rest = RestAPI()
    res, status = rest.LogIn("https://127.0.0.1:5000","3333","ophir")
    if(status==200) :
        token = res.json()['token']
   
    
    res, status = rest.UploadPic("http://127.0.0.1:5000", 100,r"C:\Users\OY\Pictures\Camera Roll\1.jpg",token)
    res, status = rest.GetDataAll("http://127.0.0.1:5000")
    res, status = rest.LogIn("http://127.0.0.1:5000","1234","yigal") # Bad password
    res, status = rest.LogIn("http://127.0.0.1:5000", "1100", "yigal") # food password
    # if(status==200) :
    #     token = res.json()['token']
    #     res, status = rest.GetDataAll("http://127.0.0.1:5000",token)
    
    if(status==200) :
        token = res.json()['token']
    user = {"user_id": "12311", "name": "ophit stu", "per": "rw"}
    res, status = rest.AddUser("http://127.0.0.1:5000", user,"fjkfkjfk") # This will fail  
    res, status = rest.AddUser("http://127.0.0.1:5000", user,token) # This will fail  
    
    
    res, status = rest.GetDataAll("http://127.0.0.1:5000",token)
    
    res, status = rest.CompareImages("http://127.0.0.1:5000", 1, r"C:\Users\ophir\Desktop\FinalProject\test_jpg\ophir.jpeg")

    res, status = rest.UploadPic("http://127.0.0.1:5000", 100,r"C:\Users\OY\Pictures\Camera Roll\1.jpg")
    res, status = rest.UploadPic("http://127.0.0.1:5000", 100, r"C:\\Users\\oll\\2.jpg")

    res, status = rest.GetDataAll("http://127.0.0.1:5000")
    print(status, res)

    (res, status) = rest.GetData("http://127.0.0.1:5000", 55634)
    print(status, res)

    res, status = rest.DeleteUserId("http://127.0.0.1:5000", 556342)
    print(status, res)

    user = {"user_id": "12311", "name": "ophit stu", "per": "rw"}
    res, status = rest.AddUser("http://127.0.0.1:5000", user)
    print(status, res)


if __name__ == "__main__":
    main()
