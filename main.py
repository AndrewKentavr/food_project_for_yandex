# -*- coding: utf-8 -*-
# pyuic5 shit.ui -o shit.py

import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from email_validator import *
from flask import Flask
from flask_login import LoginManager
from flask_restful import Api
from requests import post, put
from datetime import datetime

from data import users_resources, db_session, calories_history_resources, search_history_resources
from data.users import User
from food_func import *
from translator_func import *
from ui_classes.authorization import Ui_Dialog_2
from ui_classes.main_windowUI import Ui_MainWindow
from ui_classes.registration import Ui_Dialog

from ui_classes.history import Ui_Dialog_history



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
        self.register_window.setupUi(MainWindow)
        self.setupUi(MainWindow)
        self.register_window.widget_off(MainWindow)
        self.widget_off()
        self.login_window.widget_on(MainWindow)

        self.login_window.auth_btn.clicked.connect(self.authorization)
        self.login_window.reg_btn.clicked.connect(self.registration_switch)
        self.register_window.register_button.clicked.connect(self.registration)
        self.register_window.cancel_button.clicked.connect(self.login_switch)
        self.btn_info_recipe.clicked.connect(self.input_search_recipes)
        self.btn_random_recipe.clicked.connect(self.output_random_recipes)
        self.btn_search_ingredients.clicked.connect(self.input_search_ingredients)
        self.menu_history.triggered.connect(self.history_window)

    def authorization(self):
        db_sess = db_session.create_session()
        try:
            self.user = db_sess.query(User).filter(User.email == self.login_window.email_line.text())[0]
            assert self.user.check_password(self.login_window.password_line.text())
            self.login_window.widget_off(MainWindow)
            self.nick_label.setText(self.user.nick_name)
            self.widget_on()
        except IndexError:
            self.login_window.error_line.setText('пароль или логин введены неккоректно')
        except AssertionError:
            self.login_window.error_line.setText('пароль или логин введены неккоректно')
        finally:
            db_sess.close()

    def history_window(self):
        self.widget_off()

    def input_search_recipes(self):
        # ВОТ ТУТ ХРАНИТЬСЯ НАЗВАНИЕ РЕЦЕПТА
        # Например: Яичница

        text = ''
        text += self.lineEdit_info_recipe.text().lower()

        if text.isspace() or not text:
            self.error_dialog.showMessage('Вы ничего не ввели')
            return 0

        if any(not c.isalnum() for c in text) or any(map(str.isdigit, text)):
            self.error_dialog.showMessage('Вы ввели недопустимые символы')
            return 0

        lang = detect_language(text)

        if lang != 'en':  # тут с помощью Api Яндекса определяется на каком языке написан запрос
            text = english_trans(text)

        recipe = search_recipes(text)

        img_url = recipe[1]

        image = QtGui.QImage()
        image.loadFromData(requests.get(img_url).content)
        pixmap_0 = QtGui.QPixmap(image)
        pixmap = pixmap_0.scaled(312, 231)

        self.litle_lable.setPixmap(pixmap)

        info_recipe = recipe_information(recipe[0])
        ingred_recipe = recipe_ingredients_id(recipe[0])
        text_ing = ''

        text_ing += 'Ingredients:' + '\n'

        for i in range(len(ingred_recipe)):
            text_ing += '-' + str(ingred_recipe[i]) + '\n'

        recipe_text = ''
        recipe_text += 'Info:' + '\n'

        recipe_text += '-' + info_recipe[0] + '\n'
        recipe_text += '-' + info_recipe[1] + '\n'
        recipe_text += '-' + info_recipe[2] + '\n'

        self.listWidget_info_recipe.clear()
        self.listWidget_info_recipe.addItem(text_ing)

        self.listWidget_info_recipe_2.clear()
        self.listWidget_info_recipe_2.addItem(recipe_text)

        put(f"http://localhost:5000/api/search_histories/{self.user.id}",
            json={'title': self.lineEdit_info_recipe.text()}).json()

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

        put(f"http://localhost:5000/api/search_histories/{self.user.id}",
            json={'title': ran_rec[0], 'date': str(datetime.now())}).json()

    def input_search_ingredients(self):

        text = ''
        text += self.lineEdit_info_ingredient.text().lower()

        if text.isspace() or not text:
            self.error_dialog.showMessage('Вы ничего не ввели')
            return 0

        if any(not c.isalnum() for c in text) or any(map(str.isdigit, text)):
            self.error_dialog.showMessage('Вы ввели недопустимые символы')
            return 0

        lang = detect_language(text)

        if lang != 'en':
            text = english_trans(text)

        ingredient = ingredient_search(text)  # [0] - id; [1] - name

        info_ing = ingredient_information(ingredient[0])

        text = ''
        text += 'Name -- ' + str(ingredient[1]) + '\n'
        text += 'Calories:' + str(info_ing['Calories']['amount']) + '\n'
        text += 'Fat:' + str(info_ing['Fat']['amount']) + '\n'
        text += 'Sugar:' + str(info_ing['Sugar']['amount']) + '\n'
        text += 'Protein:' + str(info_ing['Protein']['amount']) + '\n'

        self.listWidget_info_ingredients.clear()
        self.listWidget_info_ingredients.addItem(text)

    def registration_switch(self):
        self.login_window.widget_off(MainWindow)
        self.register_window.widget_on(MainWindow)

    def login_switch(self):
        self.register_window.widget_off(MainWindow)
        self.login_window.widget_on(MainWindow)

    def registration(self):
        if 0 < len(self.register_window.nick_line.text()) <= 40:
            if self.email_validate():
                if not self.email_in_database():
                    if self.password_check():
                        if self.register_window.password_register_line.text() == \
                                self.register_window.repeat_password_line.text():
                            user = {
                                'nick_name': self.register_window.nick_line.text(),
                                'email': self.register_window.email_register_line.text(),
                                'password': self.register_window.password_register_line.text()
                            }
                            post("http://localhost:5000/api/users", json=user).json()
                            self.register_window.widget_off(MainWindow)
                            self.login_window.widget_on(MainWindow)
                        else:
                            self.register_window.error_line.setText('пароли не совпадают')
                    else:
                        self.register_window.error_line.setText('пароль небезопасный')
                else:
                    self.register_window.error_line.setText('на такую электронную почту уже есть пользователь')
            else:
                self.register_window.error_line.setText('такой электронной почты не существует')
        else:
            self.register_window.error_line.setText('имя пользователя введено некорректно')

    def email_in_database(self):
        db_sess = db_session.create_session()
        try:
            user = db_sess.query(User).filter(User.email == self.register_window.email_register_line.text())[0]
            return True
        except IndexError:
            return False
        finally:
            db_sess.close()

    def email_validate(self):
        try:
            validate_email(self.register_window.email_register_line.text())
            return True
        except EmailSyntaxError:
            return False
        except EmailNotValidError:
            return False

    def password_check(self):
        have_digit = False
        have_letter = False
        have_big_letter = False
        for element in self.register_window.password_register_line.text():
            if element.isdigit():
                have_digit = True
            elif element.lower() != element:
                have_big_letter = True
            else:
                have_letter = True
        if have_letter and have_big_letter and have_digit and \
                len(self.register_window.password_register_line.text()) >= 8:
            return True
        return False


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
