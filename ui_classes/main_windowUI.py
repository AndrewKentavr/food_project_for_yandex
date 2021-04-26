import sys

from PyQt5 import QtCore, QtWidgets, QtGui


# класс интерфейса для основного окна
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

        self.nick_label = QtWidgets.QLabel(self.centralwidget)
        self.nick_label.setGeometry(QtCore.QRect(500, 30, 339, 20))

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
        self.btn_random_recipe.setGeometry(QtCore.QRect(20, 30, 281, 41))
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
        self.listWidget_random_recipe.setGeometry(QtCore.QRect(20, 90, 291, 351))
        self.listWidget_random_recipe.setObjectName("listWidget_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.listWidget_random_recipe_2 = QtWidgets.QListWidget(self.tab_2)
        self.listWidget_random_recipe_2.setGeometry(QtCore.QRect(380, 280, 291, 161))

        self.litle_lable_2 = QtWidgets.QLabel(self.tab_2)
        self.litle_lable_2.setGeometry(QtCore.QRect(400, 40, 312, 231))

        # ---------------------TAB 3-------------------------------------------

        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_4")
        self.btn_search_ingredients = QtWidgets.QPushButton(self.tab_3)
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

        self.listWidget_info_ingredients_2 = QtWidgets.QListWidget(self.tab_3)
        self.listWidget_info_ingredients_2.setGeometry(QtCore.QRect(350, 0, 170, 441))
        self.listWidget_info_ingredients_2.setObjectName("listWidget_5")

        self.lineEdit_info_ingredient = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_info_ingredient.setGeometry(QtCore.QRect(20, 20, 281, 31))
        self.lineEdit_info_ingredient.setStyleSheet("background: white; border: 2px solid #13bd4b;")
        self.lineEdit_info_ingredient.setText("")
        self.lineEdit_info_ingredient.setObjectName("lineEdit_2")

        self.listWidget_info_ingredients = QtWidgets.QListWidget(self.tab_3)
        self.listWidget_info_ingredients.setGeometry(QtCore.QRect(20, 130, 311, 201))
        self.listWidget_info_ingredients.setObjectName("listWidget_6")

        self.listWidget_info_ingredients_3 = QtWidgets.QListWidget(self.tab_3)
        self.listWidget_info_ingredients_3.setGeometry(QtCore.QRect(530, 0, 170, 441))
        self.listWidget_info_ingredients_3.setObjectName("listWidget_7")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 753, 30))
        self.menubar.setStyleSheet("background: white; border: 2px solid #13bd4b;")
        self.menubar.setObjectName("menubar")
        self.menu_history = QtWidgets.QMenu(self.menubar)
        self.menu_history.addAction(QtWidgets.QAction("&Open", MainWindow))
        self.menu_history.setStyleSheet("")
        self.menu_history.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu_history.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.error_dialog = QtWidgets.QErrorMessage()
        self.error_dialog.setGeometry(700, 400, 150, 150)

    def widget_off(self):
        self.centralwidget.close()
        self.menubar.close()

    def widget_on(self, window):
        window.resize(753, 711)
        self.centralwidget.show()
        self.menubar.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "window"))
        self.nick_label.setText(_translate("MainWindow", ""))
        self.tabWidget.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.btn_info_recipe.setText(_translate("MainWindow", "Посмотреть сведения о еде"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Info Rec"))
        self.btn_random_recipe.setText(_translate("MainWindow", "Предложить рандомный рецепт"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Random Rec"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Info Ing"))
        self.menu_history.setTitle(_translate("MainWindow", "История поиска"))
        self.btn_search_ingredients.setText(_translate("MainWindow", "Посмотреть сведения об ингридиенте"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ex = Ui_MainWindow()
    ex.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
