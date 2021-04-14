# -*- coding: utf-8 -*-
# pyuic5 shit.ui -o shit.py


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from food_func import *
from translator_func import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(753, 711)
        MainWindow.setStyleSheet("background:#e9fadc;")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 30, 731, 341))
        self.tabWidget.setObjectName("tabWidget")

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.listWidget_info_recipe = QtWidgets.QListWidget(self.tab)
        self.listWidget_info_recipe.setGeometry(QtCore.QRect(20, 140, 281, 151))
        self.listWidget_info_recipe.setObjectName("listWidget")

        self.btn_info_recipe = QtWidgets.QPushButton(self.tab)
        self.btn_info_recipe.setGeometry(QtCore.QRect(20, 80, 281, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_info_recipe.sizePolicy().hasHeightForWidth())
        self.btn_info_recipe.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_info_recipe.setFont(font)
        self.btn_info_recipe.setStyleSheet("background: white; border: 2px solid #13bd4b;")
        self.btn_info_recipe.setObjectName("pushButton")
        self.btn_info_recipe.clicked.connect(self.input_search_recipes)

        self.lineEdit_info_recipe = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_info_recipe.setGeometry(QtCore.QRect(20, 30, 281, 31))
        self.lineEdit_info_recipe.setStyleSheet("background: white; border: 2px solid #13bd4b;")
        self.lineEdit_info_recipe.setText("")
        self.lineEdit_info_recipe.setObjectName("lineEdit")
        self.tabWidget.addTab(self.tab, "")

        self.litle_lable = QtWidgets.QLabel(self.tab)
        self.litle_lable.setGeometry(QtCore.QRect(400, 40, 312, 231))

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.btn_random_recipe = QtWidgets.QPushButton(self.tab_2)
        self.btn_random_recipe.setGeometry(QtCore.QRect(10, 30, 281, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_random_recipe.sizePolicy().hasHeightForWidth())
        self.btn_random_recipe.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_random_recipe.setFont(font)
        self.btn_random_recipe.setStyleSheet("background: white; border: 2px solid #13bd4b;")
        self.btn_random_recipe.setObjectName("pushButton_5")
        self.btn_random_recipe.clicked.connect(self.output_random_recipes)

        self.listWidget_random_recipe = QtWidgets.QListWidget(self.tab_2)
        self.listWidget_random_recipe.setGeometry(QtCore.QRect(10, 90, 281, 161))
        self.listWidget_random_recipe.setObjectName("listWidget_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.litle_lable_2 = QtWidgets.QLabel(self.tab_2)
        self.litle_lable_2.setGeometry(QtCore.QRect(400, 40, 312, 231))

        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.lineEdit_calor_for_day = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_calor_for_day.setGeometry(QtCore.QRect(10, 210, 281, 31))
        self.lineEdit_calor_for_day.setStyleSheet("background: white; border: 2px solid #13bd4b;")
        self.lineEdit_calor_for_day.setText("")
        self.lineEdit_calor_for_day.setObjectName("lineEdit_3")
        self.btn_cal_for_day = QtWidgets.QPushButton(self.tab_3)
        self.btn_cal_for_day.setGeometry(QtCore.QRect(10, 170, 241, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cal_for_day.sizePolicy().hasHeightForWidth())
        self.btn_cal_for_day.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_cal_for_day.setFont(font)
        self.btn_cal_for_day.setStyleSheet("background: white; border: 2px solid #13bd4b;")
        self.btn_cal_for_day.setObjectName("pushButton_7")
        self.label_calories = QtWidgets.QLabel(self.tab_3)
        self.label_calories.setGeometry(QtCore.QRect(10, 30, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_calories.setFont(font)
        self.label_calories.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_calories.setAutoFillBackground(False)
        self.label_calories.setStyleSheet("background: white; border: 2px solid #13bd4b;")
        self.label_calories.setWordWrap(False)
        self.label_calories.setObjectName("label")
        self.tabWidget.addTab(self.tab_3, "")

        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_your_recipe = QtWidgets.QLabel(self.tab_4)
        self.label_your_recipe.setGeometry(QtCore.QRect(40, 40, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_your_recipe.setFont(font)
        self.label_your_recipe.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_your_recipe.setAutoFillBackground(False)
        self.label_your_recipe.setStyleSheet("background: white; border: 2px solid #13bd4b;")
        self.label_your_recipe.setWordWrap(False)
        self.label_your_recipe.setObjectName("label_2")
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 753, 30))
        self.menubar.setStyleSheet("background: white; border: 2px solid #13bd4b;")
        self.menubar.setObjectName("menubar")
        self.menu_history = QtWidgets.QMenu(self.menubar)
        self.menu_history.setStyleSheet("")
        self.menu_history.setObjectName("menu")
        self.menu_stat = QtWidgets.QMenu(self.menubar)
        self.menu_stat.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu_history.menuAction())
        self.menubar.addAction(self.menu_stat.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.btn_info_recipe.setText(_translate("MainWindow", "Посмотреть сведения о еде"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Info R"))
        self.btn_random_recipe.setText(_translate("MainWindow", "Предложить рандомный рецепт"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Random R"))
        self.btn_cal_for_day.setText(_translate("MainWindow", "Ввести калория за день"))
        self.label_calories.setText(_translate("MainWindow", "Учёт калорий"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Calor"))
        self.label_your_recipe.setText(_translate("MainWindow", "Свои рецепты"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Your R"))
        self.menu_history.setTitle(_translate("MainWindow", "История поиска"))
        self.menu_stat.setTitle(_translate("MainWindow", "Статистика"))

    def input_search_recipes(self):
        text = ''
        text += self.lineEdit_info_recipe.text().lower()

        lang = detect_language(text)

        if lang != 'en':
            text = english_trans(text)

        recipe = search_recipes(text)

        img_url = recipe[1]

        image = QtGui.QImage()
        image.loadFromData(requests.get(img_url).content)
        pixmap_0 = QtGui.QPixmap(image)
        pixmap = pixmap_0.scaled(312, 231)

        self.litle_lable.setPixmap(pixmap)

        info_recipe = recipe_information(recipe[0])
        finale_text = ''
        finale_text += info_recipe[0] + '\n'
        finale_text += info_recipe[1] + '\n'
        finale_text += info_recipe[2] + '\n'

        self.listWidget_info_recipe.clear()
        self.listWidget_info_recipe.addItem(finale_text)

    def output_random_recipes(self):
        ran_rec = random_recipes()

        text = ''
        text += '----- ' + ran_rec[0] + ' -----\n'
        text += ran_rec[2] + '\n'
        text += ran_rec[3] + '\n'
        text += ran_rec[4] + '\n'

        image = QtGui.QImage()
        image.loadFromData(requests.get(ran_rec[1]).content)

        pixmap_0 = QtGui.QPixmap(image)
        pixmap = pixmap_0.scaled(312, 231)

        self.litle_lable_2.setPixmap(pixmap)

        self.listWidget_random_recipe.clear()
        self.listWidget_random_recipe.addItem(text)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ex = Ui_MainWindow()
    ex.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
