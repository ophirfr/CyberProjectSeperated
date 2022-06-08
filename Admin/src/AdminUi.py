import json
from PyQt5 import  QtWidgets
from PyQt5.QtWidgets import *
import sys
import AdminScreen
from AddUserScreen import Ui_AddUserDlg
from DeleteUserScreen import Ui_DialogDelete
from ListUsers import Ui_DialogList
from RestAPI import RestAPI
from PyQt5.QtWidgets import QMessageBox
from GetById import  Ui_Ui_DialogGetByID
import AdminLogin
from UIState import UI_State



restApi = RestAPI()
STATE = UI_State()
SERVER_URL =""
#TOKEN=""






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

def MessageBox( message):
    msgBox = QMessageBox()
    msgBox.setWindowTitle("msg")
    msgBox.setText(message)
    x = msgBox.exec_()

    # --------------------------------------------------





#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# add user screen
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

class AddUserDlg(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_AddUserDlg()
        self.ui.setupUi(self)
        self.ui.comboBox.addItem("read only")
        self.ui.comboBox.addItem("read / write")


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#get user by id screen
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

class GetUserDlg(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Ui_DialogGetByID()
        self.ui.setupUi(self)



#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# delete user by id screen
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

class DeleteUserDlg(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_DialogDelete()
        self.ui.setupUi(self)


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# list all users screen
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

class ListUsersDlg(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_DialogList()
        self.ui.setupUi(self)

        self.ui.tableWidget.setItem(0, 0, QTableWidgetItem("Id"))
        self.ui.tableWidget.setItem(0, 1, QTableWidgetItem("Name"))
        self.ui.tableWidget.setItem(0, 2, QTableWidgetItem("Permission"))


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

class LoginScreen(QtWidgets.QMainWindow, AdminLogin.Ui_AdminLogin):
    def __init__(self, parent=None):
        super(LoginScreen, self).__init__(parent)
        self.initUI()
        self.Token=""
        
        
    def initUI(self):
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button_clicked_sumbit)
        self.pushButton_2.clicked.connect(self.button_clicked_cancel)

    def button_clicked_sumbit(self):
        userName=self.lineEdit_2.text()
        password=self.lineEdit.text()
        data, status =restApi.LogIn(SERVER_URL, password , userName)
        if status==500:
            MessageBox(data)
            return
        if status != 200:
            MessageBox("You don't have access")
            return

        else :
            self.Token = data.json()['token']
            STATE.SetState(UI_State.STATE_VALID_TOKEN)
        self.lineEdit_2.setText('')
        self.lineEdit.setText('')
        self.close()
        
    def GetToken(self):
        return self.Token
    
    def button_clicked_cancel(self):
        STATE.SetState(UI_State.STATE_EXIT_APP)
        self.close()
        
            
            
    def MessageBox(self,message):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("msg")
        msgBox.setText(message)
        x = msgBox.exec_()

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


class AdminScreen(QtWidgets.QMainWindow, AdminScreen.Ui_MainWindow):
    def __init__(self,token, parent=None):
        super(AdminScreen, self).__init__(parent)
        QMainWin = QtWidgets.QMainWindow
        self.initUI()
        self.isPressed = 0
        self.Token = token

    def IsHttpTokenExpCode(self, status):
        if status == 401:
            MessageBox("Token Expired\nCan not add this user")
            STATE.SetState(UI_State.STATE_NO_TOKEN)
            self.closeMainWin()
            return True
        return False

    def IsHttpErrorCodeOk(self,status):
        if status >= 200 and status < 300:
            return True
        return False

 # --------------------------------------------------

    def initUI(self):
        self.setupUi(self)
        self.button1.clicked.connect(self.button_clicked_add)
        self.button2.clicked.connect(self.button_clicked_Del)
        self.button3.clicked.connect(self.button_clicked_List)
        self.button3_2.clicked.connect(self.button_clicked_GetByID)

    def closeEvent(self, event):
        if self.isPressed == 0:
            STATE.SetState(UI_State.STATE_EXIT_APP)
        self.isPressed = 0
        #self.event.accept()  # let the window close

    def closeMainWin(self) :
        self.isPressed = 1
        self.close()
#--------------------------------------------------

    def button_clicked_add(self):
        Dialog = AddUserDlg()
        Dialog.exec()
        name=Dialog.ui.lineEdit_2.text()
        Id = Dialog.ui.lineEdit_3.text()
        if (Id == "" or Id.isdigit() == False):
            MessageBox("Invalid ID")
            return
                    
        per=Dialog.ui.comboBox.currentText()
        picPath=Dialog.ui.lineEdit.text()
        #olderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')

        resp,status = self.uplodePicture(int(Id),picPath, self.Token)
        if (self.IsHttpTokenExpCode(status)) :
            return
        if(self.IsHttpErrorCodeOk(status) == False) :
            MessageBox("Image file not found..")
            return
        READ_ONLY = "read only"
        if(per == READ_ONLY):
            perDB="RO"
        else:
            perDB = "RW"

        user = {"user_id": Id, "name": name, "per": perDB}
        data, status =restApi.AddUser(SERVER_URL,user,self.Token)
        if (self.IsHttpTokenExpCode(status)):
            return
        if( self.IsHttpErrorCodeOk(status) ):
            MessageBox("User successfully added")
        else :
            MessageBox("Can not add this user")

# --------------------------------------------------

    def button_clicked_folder(self):
        fName = QFileDialog.getOpenFileNames(self, "open file", "", "All Files (*);; Python Files(*.py)")
        if fName:
            self.label1.setText(str(fName))

# --------------------------------------------------

    def button_clicked_Del(self):
        Dialog = DeleteUserDlg()
        Dialog.exec()
        id = Dialog.ui.lineEdit.text()
        
        
        if (str(id) == "" or id.isdigit() == False):
            MessageBox("Invalid ID")
            return

        data, status = self.DeletePic(int(id),self.Token)
        if (self.IsHttpTokenExpCode(status)):
            return

        data, status = restApi.DeleteUserId(SERVER_URL, int(id),self.Token)
        if (self.IsHttpTokenExpCode(status)):
            return

        if (status == 200):
            MessageBox("success")
            print(data)

# --------------------------------------------------
    def button_clicked_List(self):
        dlg = ListUsersDlg()
        data, status = restApi.GetDataAll(SERVER_URL )
        dlg.ui.tableWidget.setRowCount(len(data)+1)
        cnt = 0
        for x in data:
            cnt = cnt + 1
            id = x[0]
            name = x[1]
            per = x[2]
            dlg.ui.tableWidget.setItem(cnt, 0, QTableWidgetItem(str(id)))
            dlg.ui.tableWidget.setItem(cnt, 1, QTableWidgetItem(str(name)))
            dlg.ui.tableWidget.setItem(cnt, 2, QTableWidgetItem(str(per)))
        dlg.exec()

# --------------------------------------------------
    def button_clicked_GetByID(self):
        dlg = GetUserDlg()
        dlg.exec()
        id = dlg.ui.lineEdit.text()
        if (str(id) == "" or id.isdigit() == False):
            MessageBox("Invalid ID")
            return
        data, status = restApi.GetData(SERVER_URL, id )
        print(status)
        print(data)
        if (status == 200):
            data1 = str(data[0])
            MessageBox(data1)
        else:
            MessageBox("fail , please try again")
            print("fail")

 # --------------------------------------------------

    def DeletePic(self,id , token):
        data, status = restApi.DeleteFolderByID(SERVER_URL, id ,token)
        return data, status

# --------------------------------------------------

    def uplodePicture(self,id,path,token):
        data , status = restApi.UploadPic(SERVER_URL,id,path,token)
        return data,status


def main():
    IpConfig()
    #log in
    app = QApplication(sys.argv)
    global STATE


    while STATE.GetState() != UI_State.STATE_EXIT_APP:

        formLogin = LoginScreen()
        # Continue loop until U/P are correct
        while STATE.GetState() == UI_State.STATE_NO_TOKEN :
            formLogin.show()
            app.exec_()
        token = formLogin.GetToken()
        # Enter main Admin UI
        if STATE.GetState() == UI_State.STATE_VALID_TOKEN:
            # admin ui
            
            formMain = AdminScreen(token)
            formMain.show()
            app.exec_()




if __name__ == '__main__':
    main()

