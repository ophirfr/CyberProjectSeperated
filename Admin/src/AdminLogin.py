# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\OY\Desktop\ophir\FinalProject\ui\AdminLogin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
# יוצר את מסך ההתחברות של המנהל
class Ui_AdminLogin(object):
    def setupUi(self, AdminLogin):
        AdminLogin.setObjectName("AdminLogin")
        AdminLogin.resize(459, 307)
        self.centralwidget = QtWidgets.QWidget(AdminLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 10, 171, 51))
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(140, 100, 211, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(18, 110, 121, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 111, 21))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 230, 115, 33))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 230, 115, 33))
        self.pushButton_2.setObjectName("pushButton_2")
        AdminLogin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AdminLogin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 459, 21))
        self.menubar.setObjectName("menubar")
        AdminLogin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AdminLogin)
        self.statusbar.setObjectName("statusbar")
        AdminLogin.setStatusBar(self.statusbar)

        self.retranslateUi(AdminLogin)
        QtCore.QMetaObject.connectSlotsByName(AdminLogin)

    def retranslateUi(self, AdminLogin):
        _translate = QtCore.QCoreApplication.translate
        AdminLogin.setWindowTitle(_translate("AdminLogin", "MainWindow"))
        self.label.setText(_translate("AdminLogin", "Admin Login"))
        self.label_2.setText(_translate("AdminLogin", "User Name"))
        self.label_3.setText(_translate("AdminLogin", "Password"))
        self.pushButton.setText(_translate("AdminLogin", "Submit"))
        self.pushButton_2.setText(_translate("AdminLogin", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminLogin = QtWidgets.QMainWindow()
    ui = Ui_AdminLogin()
    ui.setupUi(AdminLogin)
    AdminLogin.show()
    sys.exit(app.exec_())

