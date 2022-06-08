
from PyQt5 import  QtWidgets
from PyQt5.QtWidgets import *
import sys
import LogInScreen
from RestAPI import RestAPI
from faceD import faceDetect
import json
import ctypes

restAPI= RestAPI()
faceD= faceDetect()
SERVER_URL =""
#log in screen
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def IpConfig():
    # Opening JSON file
    try:
        with open('../setting_client/IpConfig.json', 'r') as openfile:
            json_object = json.load(openfile)
    except FileNotFoundError:
        print('can not find the file')
        return
    global SERVER_URL
    SERVER_URL='https://'+json_object["ip"]+':'+json_object["port"]
    print(SERVER_URL)



class ClientUi(QtWidgets.QMainWindow, LogInScreen.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ClientUi, self).__init__(parent)
        self.initUI()

# --------------------------------------------------

    def initUI(self):
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button_clicked)

# --------------------------------------------------

# --------------------------------------------------
#input- the message you want to print
#output- Messege Box with the message
# --------------------------------------------------
    def MessegeBox(self,message):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("msg")
        msgBox.setText(message)
        msgBox.exec_()

# --------------------------------------------------
# הפונקציה נקראת כאשר המשתמש לוחץ על הכפתור
#GetDataהפונקציה מביאה את הID מה lineEdit בודקת האם ה ID תקין על ידי קריאה לפונקציה
#הפונקציה קוראת לפונקציה CompareImages שמחזירה האם המשתמש מאושר או לא ומחזירה הודעה בהתאם
# --------------------------------------------------

    def button_clicked(self):
        id= self.lineEdit.text()
        if (id == "" or id.isdigit() == False):
            self.MessegeBox("Invalid ID.\nUse numbers only")
        else:
            res,status = restAPI.GetData(SERVER_URL,int(id))
            if status==500:
                self.MessegeBox(res)
                return
            if status == 400:
                self.MessegeBox("Cound not find ID in DB")
            else:
                detectedFaces=faceD.startCapture()
                if(detectedFaces!=0):
                    res,status = restAPI.CompareImages(SERVER_URL,int(id),r"..\pic_tmp_client\face.jpg")
                    if(status== 200):
                        self.MessegeBox("You are APPROVED")
                    else:
                        self.MessegeBox("You are DENIED!!!\nThe Computer will Lockdown !!!\n You will have to re-enter your User/Pass for Windows")
                        dll = ctypes.WinDLL('user32.dll')
                        dll.LockWorkStation()
                        
                else:
                    self.MessegeBox("can not detect faces, try again")


# הרצה של הגרפיקה
def main():
    IpConfig()
    app = QApplication(sys.argv)
    form = ClientUi()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()