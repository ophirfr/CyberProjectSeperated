# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ophir\PycharmProjects\facedetectionexample\pictures\DeleteUserScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


# יוצר את Dialog של מחיקת משתמש
class Ui_DialogDelete(object):
    def setupUi(self, DialogDelete):
        DialogDelete.setObjectName("DialogDelete")
        DialogDelete.resize(432, 356)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogDelete)
        self.buttonBox.setGeometry(QtCore.QRect(-20, 270, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_2 = QtWidgets.QLabel(DialogDelete)
        self.label_2.setGeometry(QtCore.QRect(530, 340, 181, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(DialogDelete)
        self.label_3.setGeometry(QtCore.QRect(420, 440, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(DialogDelete)
        self.label.setGeometry(QtCore.QRect(580, 320, 55, 16))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(DialogDelete)
        self.label_4.setGeometry(QtCore.QRect(420, 480, 81, 21))
        self.label_4.setObjectName("label_4")
        self.buttonBox_2 = QtWidgets.QDialogButtonBox(DialogDelete)
        self.buttonBox_2.setGeometry(QtCore.QRect(380, 600, 341, 32))
        self.buttonBox_2.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox_2.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_2.setObjectName("buttonBox_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(DialogDelete)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(510, 420, 221, 151))
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
        self.label_5 = QtWidgets.QLabel(DialogDelete)
        self.label_5.setGeometry(QtCore.QRect(420, 530, 71, 20))
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(DialogDelete)
        self.lineEdit.setGeometry(QtCore.QRect(160, 160, 131, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_6 = QtWidgets.QLabel(DialogDelete)
        self.label_6.setGeometry(QtCore.QRect(80, 170, 55, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(DialogDelete)
        self.label_7.setGeometry(QtCore.QRect(114, 50, 201, 61))
        self.label_7.setObjectName("label_7")

        self.retranslateUi(DialogDelete)
        self.buttonBox.accepted.connect(DialogDelete.accept)
        self.buttonBox.rejected.connect(DialogDelete.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogDelete)

    def retranslateUi(self, DialogDelete):
        _translate = QtCore.QCoreApplication.translate
        DialogDelete.setWindowTitle(_translate("DialogDelete", "Dialog"))
        self.label_2.setText(_translate("DialogDelete", "<html><head/><body><p><span style=\" font-size:16pt; color:#ff0000;\">Add new user</span></p></body></html>"))
        self.label_3.setText(_translate("DialogDelete", "full name"))
        self.label_4.setText(_translate("DialogDelete", "id number"))
        self.label_5.setText(_translate("DialogDelete", "permission"))
        self.label_6.setText(_translate("DialogDelete", "user id"))
        self.label_7.setText(_translate("DialogDelete", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ff0000;\">Delete user</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogDelete = QtWidgets.QDialog()
    ui = Ui_DialogDelete()
    ui.setupUi(DialogDelete)
    DialogDelete.show()
    sys.exit(app.exec_())
