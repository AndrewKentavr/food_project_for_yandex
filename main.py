# -*- coding: utf-8 -*-
# pyuic5 shit.ui -o shit.py

from ui_classes.main_windowUI import Ui_MainWindow
from flask_login import LoginManager
from flask import Flask
from flask_restful import Api
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from data import users_resources, db_session, calories_history_resources, search_history_resources
from food_func import *
from translator_func import *

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
        self.setupUi(MainWindow)

        self.btn_info_recipe.clicked.connect(self.input_search_recipes)
        self.btn_random_recipe.clicked.connect(self.output_random_recipes)

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
    app_window = QtWidgets.QApplication(sys.argv)
    webapp = ApplicationThread(app)
    webapp.start()
    app_window.aboutToQuit.connect(webapp.terminate)
    MainWindow = QtWidgets.QMainWindow()
    ex = MainWindowCore()
    ex.setupUi(MainWindow)
    MainWindow.show()

    db_session.global_init('db/food_system.sqlite')
    sys.exit(app_window.exec_())
