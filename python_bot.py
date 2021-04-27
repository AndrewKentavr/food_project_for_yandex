#!/usr/bin/env python
# pylint: disable=C0116
# This program is dedicated to the public domain under the CC0 license.

import logging
from food_func import *
from translator_func import *

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

CHOOSING, TYPING_CHOICE_1, TYPING_CHOICE_2 = range(3)

reply_keyboard = [['Информация рецептов', 'Рандомный рецепт', 'Информация ингредиентов']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)


def start(update: Update, _: CallbackContext):
    update.message.reply_text(
        "Ну и что ты тут сидишь, а блин?",
        reply_markup=markup,
    )

    return CHOOSING


def wait_func(update: Update, _: CallbackContext):
    update.message.reply_text('Введите, что вам нужно')
    if update.message.text == 'Информация рецептов':
        return TYPING_CHOICE_1
    else:
        return TYPING_CHOICE_2


def rec_info(update: Update, _: CallbackContext):
    text = update.message.text

    lang = detect_language(text)

    if lang != 'en':  # тут с помощью Api Яндекса определяется на каком языке написан запрос
        text = english_trans(text)

    recipe = search_recipes(text)

    if recipe == 'AssertionError' or recipe == 'IndexError':
        update.message.reply_text("Неправильный запрос, введите ещё раз")
        return CHOOSING

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

    update.message.reply_text(recipe_text)
    update.message.reply_text(text_ing)

    return CHOOSING


def ran_recipe(update: Update, _: CallbackContext) -> int:
    ran_rec = random_recipes()

    while ran_rec == 'AssertionError':
        ran_rec = random_recipes()

    ingred_random_recipe = recipe_ingredients_id(ran_rec[5])

    text_ing = ''
    text_ing += 'Ingredients:' + '\n'
    for i in range(len(ingred_random_recipe)):
        text_ing += '-' + str(ingred_random_recipe[i]) + '\n'

    recipe_text = ''
    recipe_text += '----- ' + ran_rec[0] + ' -----\n'
    recipe_text += 'Info:' + '\n'
    recipe_text += ran_rec[2] + '\n'
    recipe_text += ran_rec[3] + '\n'
    recipe_text += ran_rec[4] + '\n'

    update.message.reply_text(recipe_text)
    update.message.reply_text(text_ing)

    return CHOOSING


def ing_info(update: Update, _: CallbackContext):
    text = update.message.text

    lang = detect_language(text)

    if lang != 'en':  # тут с помощью Api Яндекса определяется на каком языке написан запрос
        text = english_trans(text)

    ingredient = ingredient_search(text)  # [0] - id; [1] - name

    if ingredient == 'AssertionError' or ingredient == 'IndexError':
        update.message.reply_text("Неправильный запрос, введите ещё раз")
        return CHOOSING

    info_ing = ingredient_information(ingredient[0])

    text_1 = ''
    text_1 += 'Name -- ' + str(ingredient[1]) + '\n'
    text_1 += 'Calories: ' + str(info_ing['Calories']['amount']) + '\n'
    text_1 += 'Fat: ' + str(info_ing['Fat']['amount']) + '\n'
    text_1 += 'Sugar: ' + str(info_ing['Sugar']['amount']) + '\n'
    text_1 += 'Protein: ' + str(info_ing['Protein']['amount']) + '\n'

    text_2 = ''

    for i in info_ing:
        if i == 'Calories' or i == 'Fat' or i == 'Sugar' or i == 'Protein':
            continue
        else:
            text_2 += i + ': ' + str(info_ing[i]['amount']) + '\n'

    update.message.reply_text(text_1)
    update.message.reply_text(text_2)

    return CHOOSING


def cancel(update: Update, _: CallbackContext) -> int:
    pass


def main() -> None:
    updater = Updater(Globals.telegram_token)
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CHOOSING: [
                MessageHandler(Filters.regex('^Информация рецептов$'), wait_func),
                MessageHandler(Filters.regex('^Информация ингредиентов$'), wait_func),
                MessageHandler(Filters.regex('^Рандомный рецепт$'), ran_recipe)
            ],
            TYPING_CHOICE_1: [
                MessageHandler(Filters.text & ~(Filters.command | Filters.regex('^Done$')), rec_info)
            ],
            TYPING_CHOICE_2: [
                MessageHandler(Filters.text & ~(Filters.command | Filters.regex('^Done$')), ing_info)
            ],
        },

        fallbacks=[CommandHandler('cancel', cancel)],

    )

    # reply_keyboard = [['Информация рецептов', 'Рандомный рецепт', 'Информация ингредиентов']]

    dispatcher.add_handler(conv_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
