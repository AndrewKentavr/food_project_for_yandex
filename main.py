# -*- coding: utf-8 -*-
# pyuic5 shit.ui -o shit.py
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from flask import Flask
from flask_login import LoginManager, current_user, login_user
from flask_restful import Api
from requests import post
from validate_email import validate_email
from ui_classes.authorization import Ui_Dialog_2

from data import users_resources, db_session, calories_history_resources, search_history_resources
from data.users import User
from food_func import *
from translator_func import *
from ui_classes.main_windowUI import Ui_MainWindow
from ui_classes.registration import Ui_Dialog


def my_excepthook(type, value, tback):
    QtWidgets.QMessageBox.critical(
        window, "CRITICAL ERROR", str(value),
        QtWidgets.QMessageBox.Cancel
    )

    sys.__excepthook__(type, value, tback)


sys.excepthook = my_excepthook

app = Flask(__name__)
api = Api(app)

api.add_resource(users_resources.UserListResource, '/api/users')
api.add_resource(users_resources.UserResource, '/api/users/<int:user_id>')
api.add_resource(search_history_resources.SearchHistoryListResource, '/api/search_histories')
api.add_resource(search_history_resources.SearchHistoryResource, '/api/search_histories/<int:history_id>')
api.add_resource(calories_history_resources.CaloriesHistoryListResource, '/api/search_histories')
api.add_resource(calories_history_resources.CaloriesHistoryResource, '/api/search_histories/<int:history_id>')

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/')
def index():
    return None


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


class ApplicationThread(QtCore.QThread):
    def __init__(self, application, port=5000):
        super(ApplicationThread, self).__init__()
        self.application = application
        self.port = port

    def __del__(self):
        self.wait()

    def run(self):
        self.application.run(port=self.port, threaded=True)


class MainWindowCore(Ui_MainWindow):
    def __init__(self):
        self.user = None
        self.login_window = Ui_Dialog_2()
        self.register_window = Ui_Dialog()
        self.login_window.setupUi(MainWindow)
        self.login_window.auth_btn.clicked.connect(self.authorization)
        self.login_window.reg_btn.clicked.connect(self.registration)

    def authorization(self):
        db_sess = db_session.create_session()
        self.user = db_sess.query(User).get(self.login_window.email_line.text())
        if self.user and self.user.check_password(self, self.login_window.password_line):
            self.login_window.widget.hide()
            Ui_MainWindow.setupUi(self, MainWindow)

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

    def registration(self):
        self.login_window.widget_switch()
        self.register_window.setupUi(MainWindow)
        if validate_email(self.register_window.email_line.text()) and \
                self.register_window.lineEdit_6.text() == self.register_window.lineEdit_6.text():
            user = {
                'nick_name': self.register_window.lineEdit_4.text(),
                'email': self.register_window.email_line.text(),
                'password': self.register_window.lineEdit_6.text()
            }
            post("http://localhost:5000/api/users", json=user).json()
            self.register_window.widget.hide()
            self.login_window.setupUi(MainWindow)

    def login(self):
        pass


if __name__ == '__main__':
    app_window = QtWidgets.QApplication(sys.argv)
    db_session.global_init('db/food_system.sqlite')
    webapp = ApplicationThread(app)
    webapp.start()
    app_window.aboutToQuit.connect(webapp.terminate)
    MainWindow = QtWidgets.QMainWindow()
    ex = MainWindowCore()
    MainWindow.show()

    sys.exit(app_window.exec_())
