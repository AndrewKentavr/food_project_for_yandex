import sqlite3

# string = input().split()
# nick_name, email, password = string[0], string[1], string[2]
#
#
# def reg(nick_name, email, password):
#     con = sqlite3.connect('db_main/data_base_main.db')
#     cur = con.cursor()
#     # cur.execute(f"""INSERT INTO Users (nick_name, email, password, id_history)
#     # VALUES ("{nick_name}", "{email}", "{password}", "12");""")
#
#     cur.execute(f"""SELECT id FROM users""")
#     value = cur.fetchall()
#     print(value)
#     con.commit()
#     cur.close()
#     con.close()
#
#
# reg(nick_name, email, password)
# from datetime import datetime
# name = 'jopa'
# description = 'jopa'
#
#
# con = sqlite3.connect('db_main/data_base_main.db')
# cur = con.cursor()
# cur.execute(f"""INSERT INTO History (time, id_user, name, description)
# VALUES ("{str(datetime.now())}", "2", "{name}", "{description}");""")
#
# # cur.execute(f"""SELECT email, password FROM users""")
# # cat = cur.fetchall()
# # value = [cat[i] for i in range(len(cat))]
# # print(value)
# con.commit()
# cur.close()
# con.close()
#
# for i in value:
#     if 'vl' in i:
#         if i[1] == 'j714827':
#             print(i)
# n = 1
#
# con = sqlite3.connect('db_main/data_base_main.db')
# cur = con.cursor()
# cur.execute(f"""SELECT search, name, what_is, time FROM history
# WHERE id_user = '{n}';""")
# cat = cur.fetchall()
# cur.close()
# con.close()
# history = ['\t'.join(element) for element in cat]
# print(history)

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'history_shit.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import json
import sys

from PyQt5 import QtCore, QtGui, QtWidgets


# класс интерфйеса для окна истории поиска
class Ui_Dialog_history(object):
    def setupUi(self, Dialog):
        self.list_history = QtWidgets.QListView(Dialog)
        self.list_history.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.list_history.setGeometry(QtCore.QRect(10, 10, 520, 680))
        self.list_history.setStyleSheet("background: white; border: 2px solid #13bd4b;")
        self.list_history.setObjectName("list_history")
        self.btn_exit = QtWidgets.QPushButton(Dialog)
        self.btn_exit.setGeometry(QtCore.QRect(380, 700, 150, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.btn_exit.setFont(font)
        self.btn_exit.setStyleSheet("background: white; border: 2px solid #13bd4b;")
        self.btn_exit.setObjectName("btn_exit")
        self.btn_clear_all = QtWidgets.QPushButton(Dialog)
        self.btn_clear_all.setGeometry(QtCore.QRect(10, 700, 160, 31))
        self.btn_clear_all.setFont(font)
        self.btn_clear_all.setStyleSheet("background: white; border: 2px solid #13bd4b;")
        self.btn_clear_all.setObjectName("btn_clear_all")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_exit.setText(_translate("Dialog", "Выйти"))
        self.btn_clear_all.setText(_translate("Dialog", "Очистить историю"))

    def widget_off(self):
        self.btn_clear_all.close()
        self.btn_exit.close()
        self.list_history.close()

    def widget_on(self, dialog, history):
        dialog.resize(540, 760)
        self.btn_exit.show()

        history_0 = history

        history = []

        for element in history_0:
            tt = []
            for i in element:
                if len(i) > 17:
                    tt.append(i[0:17] + '..')
                else:
                    tt.append(i)
            tt = '\t'.join(tt)
            history.append(tt)

        model = QtGui.QStandardItemModel()
        self.list_history.setModel(model)
        for element in history:
            item = QtGui.QStandardItem(element)
            model.appendRow(item)
        self.list_history.show()

        self.btn_clear_all.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ex = Ui_Dialog_history()
    ex.setupUi(MainWindow)
    MainWindow.show()
    ex.widget_on(MainWindow, '[]')
    sys.exit(app.exec_())
