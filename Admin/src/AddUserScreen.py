# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ophir\Documents\GitHub\final_prj\final_project\FinalProject\ui\AddUserScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

# יוצר את מסך הוספת משתמש

class Ui_AddUserDlg(object):
    def setupUi(self, AddUserDlg):
        AddUserDlg.setObjectName("AddUserDlg")
        AddUserDlg.resize(472, 403)
        self.okB = QtWidgets.QDialogButtonBox(AddUserDlg)
        self.okB.setGeometry(QtCore.QRect(150, 330, 191, 32))
        self.okB.setOrientation(QtCore.Qt.Horizontal)
        self.okB.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.okB.setObjectName("okB")
        self.label = QtWidgets.QLabel(AddUserDlg)
        self.label.setGeometry(QtCore.QRect(220, 20, 55, 16))
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(AddUserDlg)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(100, 130, 281, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(AddUserDlg)
        self.label_2.setGeometry(QtCore.QRect(140, 40, 201, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(AddUserDlg)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(AddUserDlg)
        self.label_4.setGeometry(QtCore.QRect(20, 180, 81, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(AddUserDlg)
        self.label_5.setGeometry(QtCore.QRect(20, 220, 71, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(AddUserDlg)
        self.label_6.setGeometry(QtCore.QRect(20, 260, 91, 21))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(AddUserDlg)
        self.label_7.setGeometry(QtCore.QRect(20, 260, 71, 20))
        self.label_7.setObjectName("label_7")

        self.retranslateUi(AddUserDlg)
        self.okB.rejected.connect(AddUserDlg.reject)
        self.okB.accepted.connect(AddUserDlg.accept)
        QtCore.QMetaObject.connectSlotsByName(AddUserDlg)

    def retranslateUi(self, AddUserDlg):
        _translate = QtCore.QCoreApplication.translate
        AddUserDlg.setWindowTitle(_translate("AddUserDlg", "Dialog"))
        self.label_2.setText(_translate("AddUserDlg", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; text-decoration: underline; color:#ff0000;\">Add New User</span></p></body></html>"))
        self.label_3.setText(_translate("AddUserDlg", "Full name"))
        self.label_4.setText(_translate("AddUserDlg", "ID number"))
        self.label_5.setText(_translate("AddUserDlg", "Permission"))
        self.label_7.setText(_translate("AddUserDlg", "User photo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddUserDlg = QtWidgets.QDialog()
    ui = Ui_AddUserDlg()
    ui.setupUi(AddUserDlg)
    AddUserDlg.show()
    sys.exit(app.exec_())