from PyQt5 import QtCore, QtWidgets, QtGui
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(753, 711)
        MainWindow.setStyleSheet("background:#e9fadc;")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 30, 731, 481))
        self.tabWidget.setObjectName("tabWidget")

        # ---------------------TAB 1-------------------------------------------

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.listWidget_info_recipe = QtWidgets.QListWidget(self.tab)
        self.listWidget_info_recipe.setGeometry(QtCore.QRect(20, 140, 291, 301))
        self.listWidget_info_recipe.setObjectName("listWidget")

        self.listWidget_info_recipe_2 = QtWidgets.QListWidget(self.tab)
        self.listWidget_info_recipe_2.setGeometry(QtCore.QRect(380, 340, 291, 101))
        self.listWidget_info_recipe_2.setObjectName("listWidget_4")

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

        self.lineEdit_info_recipe = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_info_recipe.setGeometry(QtCore.QRect(20, 30, 281, 31))
        self.lineEdit_info_recipe.setStyleSheet("background: white; border: 2px solid #13bd4b;")
        self.lineEdit_info_recipe.setText("")
        self.lineEdit_info_recipe.setObjectName("lineEdit")
        self.tabWidget.addTab(self.tab, "")

        self.litle_lable = QtWidgets.QLabel(self.tab)
        self.litle_lable.setGeometry(QtCore.QRect(400, 40, 312, 231))

        # ---------------------TAB 2-------------------------------------------

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

        self.listWidget_random_recipe = QtWidgets.QListWidget(self.tab_2)
        self.listWidget_random_recipe.setGeometry(QtCore.QRect(10, 90, 281, 161))
        self.listWidget_random_recipe.setObjectName("listWidget_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.litle_lable_2 = QtWidgets.QLabel(self.tab_2)
        self.litle_lable_2.setGeometry(QtCore.QRect(400, 40, 312, 231))

        # ---------------------TAB 3-------------------------------------------

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

        # ---------------------TAB 4-------------------------------------------

        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.btn_search_ingredients = QtWidgets.QPushButton(self.tab_4)
        self.btn_search_ingredients.setGeometry(QtCore.QRect(20, 70, 311, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_search_ingredients.sizePolicy().hasHeightForWidth())
        self.btn_search_ingredients.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_search_ingredients.setFont(font)
        self.btn_search_ingredients.setStyleSheet("background: white; border: 2px solid #13bd4b;")
        self.btn_search_ingredients.setObjectName("pushButton_2")

        self.listWidget_info_ingredients = QtWidgets.QListWidget(self.tab_4)
        self.listWidget_info_ingredients.setGeometry(QtCore.QRect(390, 60, 291, 381))
        self.listWidget_info_ingredients.setObjectName("listWidget_5")

        self.lineEdit_info_ingredient = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_info_ingredient.setGeometry(QtCore.QRect(20, 20, 281, 31))
        self.lineEdit_info_ingredient.setStyleSheet("background: white; border: 2px solid #13bd4b;")
        self.lineEdit_info_ingredient.setText("")
        self.lineEdit_info_ingredient.setObjectName("lineEdit_2")

        self.listWidget_info_ingredients_2 = QtWidgets.QListWidget(self.tab_4)
        self.listWidget_info_ingredients_2.setGeometry(QtCore.QRect(20, 130, 311, 201))
        self.listWidget_info_ingredients_2.setObjectName("listWidget_6")
        self.listWidget_info_ingredients_3 = QtWidgets.QListWidget(self.tab_4)
        self.listWidget_info_ingredients_3.setGeometry(QtCore.QRect(20, 340, 311, 101))
        self.listWidget_info_ingredients_3.setObjectName("listWidget_7")
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

        self.error_dialog = QtWidgets.QErrorMessage()
        self.error_dialog.setGeometry(700, 400, 150, 150)

    def widget_off(self):
        self.centralwidget.close()
        self.menubar.close()

    def widget_on(self):
        self.centralwidget.show()
        self.menubar.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "window"))
        self.tabWidget.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.btn_info_recipe.setText(_translate("MainWindow", "Посмотреть сведения о еде"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Info Rec"))
        self.btn_random_recipe.setText(_translate("MainWindow", "Предложить рандомный рецепт"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Random Rec"))
        self.btn_cal_for_day.setText(_translate("MainWindow", "Ввести калория за день"))
        self.label_calories.setText(_translate("MainWindow", "Учёт калорий"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Calor"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Info Ing"))
        self.menu_history.setTitle(_translate("MainWindow", "История поиска"))
        self.menu_stat.setTitle(_translate("MainWindow", "Статистика"))
        self.btn_search_ingredients.setText(_translate("MainWindow", "Посмотреть сведения об ингридиенте"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ex = Ui_MainWindow()
    ex.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
