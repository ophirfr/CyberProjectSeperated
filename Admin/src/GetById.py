# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ophir\PycharmProjects\facedetectionexample\pictures\GetById.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

#יוצר את הגרפיקה של ה Dialog שמביא משתמש אחד על פי המספר המזהה
class Ui_Ui_DialogGetByID(object):
    def setupUi(self, Ui_DialogGetByID):
        Ui_DialogGetByID.setObjectName("Ui_DialogGetByID")
        Ui_DialogGetByID.resize(464, 201)
        self.buttonBox = QtWidgets.QDialogButtonBox(Ui_DialogGetByID)
        self.buttonBox.setGeometry(QtCore.QRect(-10, 150, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lineEdit = QtWidgets.QLineEdit(Ui_DialogGetByID)
        self.lineEdit.setGeometry(QtCore.QRect(180, 90, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Ui_DialogGetByID)
        self.label.setGeometry(QtCore.QRect(100, 90, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Ui_DialogGetByID)
        self.label_2.setGeometry(QtCore.QRect(190, 20, 121, 20))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Ui_DialogGetByID)
        self.buttonBox.accepted.connect(Ui_DialogGetByID.accept)
        self.buttonBox.rejected.connect(Ui_DialogGetByID.reject)
        QtCore.QMetaObject.connectSlotsByName(Ui_DialogGetByID)

    def retranslateUi(self, Ui_DialogGetByID):
        _translate = QtCore.QCoreApplication.translate
        Ui_DialogGetByID.setWindowTitle(_translate("Ui_DialogGetByID", "Dialog"))
        self.label.setText(_translate("Ui_DialogGetByID", "User ID"))
        self.label_2.setText(_translate("Ui_DialogGetByID", "Get user by ID"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ui_DialogGetByID = QtWidgets.QDialog()
    ui = Ui_Ui_DialogGetByID()
    ui.setupUi(Ui_DialogGetByID)
    Ui_DialogGetByID.show()
    sys.exit(app.exec_())
