# -*- coding: utf-8 -*-
# pyuic5 shit.ui -o shit.py

from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from email_validator import *
from requests import post, put, get

from data import db_session
from data.users import User
from food_func import *
from translator_func import *
from ui_classes.authorization import Ui_Dialog_2
from ui_classes.history import Ui_Dialog_history
from ui_classes.main_windowUI import Ui_MainWindow
from ui_classes.registration import Ui_Dialog


def my_excepthook(type, value, tback):
    QtWidgets.QMessageBox.critical(
        window, "CRITICAL ERROR", str(value),
        QtWidgets.QMessageBox.Cancel
    )

    sys.__excepthook__(type, value, tback)


sys.excepthook = my_excepthook


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
        # инициализация переменных для пользователя и его истории, а также инициализация всех окон для приложения
        self.user = None
        self.history = None
        self.login_window = Ui_Dialog_2()
        self.register_window = Ui_Dialog()
        self.history_window = Ui_Dialog_history()
        self.login_window.setupUi(MainWindow)
        self.register_window.setupUi(MainWindow)
        self.history_window.setupUi(MainWindow)
        self.setupUi(MainWindow)
        self.register_window.widget_off()
        self.history_window.widget_off()
        self.widget_off()
        self.login_window.widget_on(MainWindow)
        # сигналы для окна авторизации
        self.login_window.auth_btn.clicked.connect(self.authorization)
        self.login_window.reg_btn.clicked.connect(self.registration_switch)
        # сигналы для окна регистрации
        self.register_window.register_button.clicked.connect(self.registration)
        self.register_window.cancel_button.clicked.connect(self.login_switch)
        # сигналы для окна с историей
        self.menu_history.triggered.connect(self.main_history_switch)
        self.history_window.btn_clear_all.clicked.connect(self.history_clear)
        self.history_window.btn_exit.clicked.connect(self.history_main_switch)
        #  сигналы для главного функционала программы
        self.btn_info_recipe.clicked.connect(self.input_search_recipes)
        self.btn_random_recipe.clicked.connect(self.output_random_recipes)
        self.btn_search_ingredients.clicked.connect(self.input_search_ingredients)

    # метод производит поиск пользователя в базе данных
    # если данные введены корректно, то программа получает самого пользователя и его историю
    # а также сменяется интерфейс на интерфейс основного окна
    def authorization(self):
        db_sess = db_session.create_session()
        try:
            self.user = db_sess.query(User).filter(User.email == self.login_window.email_line.text())[0]
            assert self.user.check_password(self.login_window.password_line.text())
            self.login_window.widget_off()
            self.nick_label.setText(self.user.nick_name)
            self.history = get(f"http://localhost:5000/api/search_histories/{self.user.id}").json() \
                ['searches']['history']
            self.widget_on(MainWindow)
        except IndexError:
            self.login_window.error_line.setText('пароль или логин введены неккоректно')
        except AssertionError:
            self.login_window.error_line.setText('пароль или логин введены неккоректно')
        finally:
            db_sess.close()

    # метод смены интерфейса
    def registration_switch(self):
        self.login_window.widget_off()
        self.register_window.widget_on(MainWindow)

    # метод для регистрации пользователя
    # если введённые данные проходят проверку, то создаётся новй пользователь вместе с его историей поиска
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
                            self.register_window.widget_off()
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

    # метод смены интерфейса
    def login_switch(self):
        self.register_window.widget_off()
        self.login_window.widget_on(MainWindow)

    # метод смены интерфейса
    def main_history_switch(self):
        self.widget_off()
        self.history_window.widget_on(MainWindow, self.history)

    # метод сброса истории поиска
    def history_clear(self):
        model = QtGui.QStandardItemModel()
        self.history_window.list_history.setModel(model)
        put(f"http://localhost:5000/api/search_histories/{self.user.id}",
            json={'title': 'NULL', 'date': str(datetime.now())}).json()

    # метод смены интерфейса
    def history_main_switch(self):
        self.history_window.widget_off()
        self.widget_on(MainWindow)

    def input_search_recipes(self):
        text = ''
        text += self.lineEdit_info_recipe.text().lower()

        if text.isspace() or not text:
            self.error_dialog.showMessage('Вы ничего не ввели')
            return False

        if any(not c.isalnum() for c in text) or any(map(str.isdigit, text)):
            self.error_dialog.showMessage('Вы ввели недопустимые символы')
            return False

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

        ingred_recipe = recipe_ingredients_id(recipe[0])
        text_ing = ''
        text_ing += 'Ingredients:' + '\n'
        for i in range(len(ingred_recipe)):
            text_ing += '-' + str(ingred_recipe[i]) + '\n'

        info_recipe = recipe_information(recipe[0])
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
            json={'title': self.lineEdit_info_recipe.text(), 'date': str(datetime.now())}).json()
        self.history = get(f"http://localhost:5000/api/search_histories/{self.user.id}").json() \
            ['searches']['history']

    def output_random_recipes(self):
        ran_rec = random_recipes()

        ingred_random_recipe = recipe_ingredients_id(ran_rec[5])

        text_ing = ''
        text_ing += 'Ingredients:' + '\n'
        for i in range(len(ingred_random_recipe)):
            text_ing += '-' + str(ingred_random_recipe[i]) + '\n'

        text_inf = ''
        text_inf += '----- ' + ran_rec[0] + ' -----\n'
        text_inf += 'Info:' + '\n'
        text_inf += ran_rec[2] + '\n'
        text_inf += ran_rec[3] + '\n'
        text_inf += ran_rec[4] + '\n'

        image = QtGui.QImage()
        image.loadFromData(requests.get(ran_rec[1]).content)
        pixmap_0 = QtGui.QPixmap(image)
        pixmap = pixmap_0.scaled(312, 231)
        self.litle_lable_2.setPixmap(pixmap)

        self.listWidget_random_recipe.clear()
        self.listWidget_random_recipe.addItem(text_ing)

        self.listWidget_random_recipe_2.clear()
        self.listWidget_random_recipe_2.addItem(text_inf)

        put(f"http://localhost:5000/api/search_histories/{self.user.id}",
            json={'title': ran_rec[0], 'date': str(datetime.now())}).json()
        self.history = get(f"http://localhost:5000/api/search_histories/{self.user.id}").json() \
            ['searches']['history']

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
        text += 'Calories: ' + str(info_ing['Calories']['amount']) + '\n'
        text += 'Fat: ' + str(info_ing['Fat']['amount']) + '\n'
        text += 'Sugar: ' + str(info_ing['Sugar']['amount']) + '\n'
        text += 'Protein: ' + str(info_ing['Protein']['amount']) + '\n'

        text_2 = ''
        text_3 = ''

        count = 0
        for i in info_ing:
            if i == 'Calories' or i == 'Fat' or i == 'Sugar' or i == 'Protein':
                continue
            else:
                if count < 17:
                    text_2 += i + ': ' + str(info_ing[i]['amount']) + '\n'
                else:
                    text_3 += i + ': ' + str(info_ing[i]['amount']) + '\n'

            count += 1

        self.listWidget_info_ingredients.clear()
        self.listWidget_info_ingredients.addItem(text)

        put(f"http://localhost:5000/api/search_histories/{self.user.id}",
            json={'title': ingredient[1], 'date': str(datetime.now())}).json()
        self.history = get(f"http://localhost:5000/api/search_histories/{self.user.id}").json() \
            ['searches']['history']

    # метод проверки пользователя в базе данных для функции регистрации
    def email_in_database(self):
        db_sess = db_session.create_session()
        try:
            user = db_sess.query(User).filter(User.email == self.register_window.email_register_line.text())[0]
            return True
        except IndexError:
            return False
        finally:
            db_sess.close()

    # метод на корректность адресса электронной почты
    def email_validate(self):
        try:
            validate_email(self.register_window.email_register_line.text())
            return True
        except EmailSyntaxError:
            return False
        except EmailNotValidError:
            return False

    # метод на проверку безопасности пароля
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
    MainWindow = QtWidgets.QMainWindow()
    ex = MainWindowCore()
    MainWindow.show()

    sys.exit(app_window.exec_())
