# -*- coding: utf-8 -*-
# pyuic5 shit.ui -o shit.py

from datetime import datetime
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from email_validator import *

from food_func import *
from translator_func import *
from ui_classes.authorization import Ui_Dialog_2
from ui_classes.history import Ui_Dialog_history
from ui_classes.main_windowUI import Ui_MainWindow
from ui_classes.registration import Ui_Dialog


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
        user_email = self.login_window.email_line.text()
        password = self.login_window.password_line.text()

        con = sqlite3.connect('db_main/data_base_main.db')
        cur = con.cursor()

        cur.execute(f"""SELECT email, password, nick_name, id FROM users""")
        email_and_passwords = cur.fetchall()
        value = [email_and_passwords[i] for i in range(len(email_and_passwords))]
        con.commit()
        cur.close()
        con.close()
        for i in value:
            if user_email in i:
                if password == i[1]:

                    self.login_window.widget_off()
                    self.nick_label.setText(i[2])
                    self.id_user = i[3]
                    print(self.id_user)
                    # self.history = get(f"https://food-project-lyceum.herokuapp.com"
                    #                    f"/api/search_histories/{self.user['user']['id']}").json() \
                    #     ['searches']['history']
                    self.widget_on(MainWindow)
                else:
                    self.login_window.error_line.setText('пароль или логин введены неккоректно')
            else:
                self.login_window.error_line.setText('пароль или логин введены неккоректно')

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

                            con = sqlite3.connect(Globals.db_name)
                            cur = con.cursor()
                            cur.execute(f"""INSERT INTO Users (nick_name, email, password)
                            VALUES ("{self.register_window.nick_line.text()}", "{self.register_window.email_register_line.text()}", "{self.register_window.password_register_line.text()}");""")

                            value = cur.fetchall()
                            con.commit()
                            cur.close()
                            con.close()

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

    # метод смены интерфейса на логин
    def login_switch(self):
        self.register_window.widget_off()
        self.login_window.widget_on(MainWindow)

    # метод смены интерфейса на историю
    def main_history_switch(self):
        self.widget_off()
        self.history_window.widget_on(MainWindow, self.history)

    # метод сброса истории поиска
    def history_clear(self):
        model = QtGui.QStandardItemModel()
        self.history_window.list_history.setModel(model)
        # put(f"https://food-project-lyceum.herokuapp.com/api/search_histories/{self.user['user']['id']}",
        #     json={'title': 'NULL', 'date': str(datetime.now())}).json()

    # метод смены интерфейса
    def history_main_switch(self):
        self.history_window.widget_off()
        self.widget_on(MainWindow)

    def input_search_recipes(self):
        what_is = 'recipe'
        text = ''
        text += self.lineEdit_info_recipe.text().lower()

        if text.isspace() or not text:
            self.error_dialog.showMessage('Вы ничего не ввели')
            return 0

        if any(not c.isalnum() for c in text) or any(map(str.isdigit, text)):
            if ' ' not in text:
                self.error_dialog.showMessage('Вы ввели недопустимые символы')
                return 0
        source_text = text
        lang = detect_language(text)

        if lang != 'en':  # тут с помощью Api Яндекса определяется на каком языке написан запрос
            text = english_trans(text)

        recipe = search_recipes(text)

        if recipe == 'AssertionError' or recipe == 'IndexError':
            err = 'Такого рецепта не существует'
            self.error_dialog.showMessage(err)
            self.add_history_db(str(text), err, what_is)
            return 0

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

        self.add_history_db(str(text), 'cat', what_is)


    def output_random_recipes(self):
        what_is = 'random recipes'

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

        self.add_history_db('рандомнй рецепт', ran_rec[0], what_is)


    def input_search_ingredients(self):
        what_is = 'ingredients'

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
        name = str(ingredient[1])
        if ingredient == 'AssertionError' or ingredient == 'IndexError':
            err = 'Такого ингредиента не существует'
            self.error_dialog.showMessage(err)
            self.add_history_db(str(text), err, what_is)
            return 0

        info_ing = ingredient_information(ingredient[0])

        text_1 = ''
        text_1 += 'Name -- ' + name + '\n'
        text_1 += 'Calories: ' + str(info_ing['Calories']['amount']) + '\n'
        text_1 += 'Fat: ' + str(info_ing['Fat']['amount']) + '\n'
        text_1 += 'Sugar: ' + str(info_ing['Sugar']['amount']) + '\n'
        text_1 += 'Protein: ' + str(info_ing['Protein']['amount']) + '\n'

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
        self.listWidget_info_ingredients.addItem(text_1)

        self.listWidget_info_ingredients_2.clear()
        self.listWidget_info_ingredients_2.addItem(text_2)

        self.listWidget_info_ingredients_3.clear()
        self.listWidget_info_ingredients_3.addItem(text_3)

        self.add_history_db(str(text), name, what_is)

    # метод проверки пользователя в базе данных для функции регистрации
    def email_in_database(self):
        email = self.register_window.email_register_line.text()

        con = sqlite3.connect(Globals.db_name)
        cur = con.cursor()
        cur.execute(f"""SELECT email FROM users""")
        cat = cur.fetchall()
        value = [cat[i][0] for i in range(len(cat))]
        con.commit()
        cur.close()
        con.close()

        if email in value:
            return True
        else:
            return False

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

    def add_history_db(self, search, name, what_is):
        con = sqlite3.connect('db_main/data_base_main.db')
        cur = con.cursor()
        cur.execute(f"""INSERT INTO History (time, id_user, name, search, what_is)
        VALUES ("{str(datetime.now())}", {self.id_user}, "{name}", "{search}", "{what_is}");""")
        con.commit()
        cur.close()
        con.close()


if __name__ == '__main__':
    app_window = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ex = MainWindowCore()
    MainWindow.show()

    sys.exit(app_window.exec_())
