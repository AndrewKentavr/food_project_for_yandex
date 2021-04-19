# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Dialog_2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(369, 508)
        Dialog.setStyleSheet("background: white;")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.auth_btn = QtWidgets.QPushButton(Dialog)
        self.auth_btn.setGeometry(QtCore.QRect(20, 410, 131, 31))
        self.auth_btn.setObjectName("pushButton")
        self.reg_btn = QtWidgets.QPushButton(Dialog)
        self.reg_btn.setGeometry(QtCore.QRect(220, 410, 131, 31))
        self.reg_btn.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(150, 160, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(140, 260, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.email_line = QtWidgets.QLineEdit(Dialog)
        self.email_line.setGeometry(QtCore.QRect(20, 210, 339, 29))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.email_line.sizePolicy().hasHeightForWidth())
        self.email_line.setSizePolicy(sizePolicy)
        self.email_line.setStyleSheet("background: white; border: 2px solid #13bd4b; border-radius: 8px;")
        self.email_line.setObjectName("lineEdit_5")
        self.password_line = QtWidgets.QLineEdit(Dialog)
        self.password_line.setGeometry(QtCore.QRect(20, 320, 339, 29))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_line.sizePolicy().hasHeightForWidth())
        self.password_line.setSizePolicy(sizePolicy)
        self.password_line.setStyleSheet("background: white; border: 2px solid #13bd4b; border-radius: 8px;")
        self.password_line.setObjectName("lineEdit_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.auth_btn.setText(_translate("Dialog", "Войти"))
        self.reg_btn.setText(_translate("Dialog", "Регистрация"))
        self.label_2.setText(_translate("Dialog", "email"))
        self.label_3.setText(_translate("Dialog", "password"))

    def widget_switch(self):
        self.auth_btn.close()
        self.reg_btn.close()
        self.email_line.close()
        self.password_line.close()
        self.label_2.close()
        self.label_3.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ex = Ui_Dialog_2()
    ex.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
