import logging
import os
import sys

from flask import Flask
from flask_restful import Api
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

from data import db_session
from data import users_resources, search_history_resources
from food_func import *
from translator_func import *

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)
api = Api(app)

api.add_resource(users_resources.UserListResource, '/api/users')
api.add_resource(users_resources.UserResource, '/api/users/<int:user_id>')
api.add_resource(search_history_resources.SearchHistoryListResource, '/api/search_histories')
api.add_resource(search_history_resources.SearchHistoryResource, '/api/search_histories/<int:history_id>')

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

CHOOSING = range(1)

reply_keyboard = [['Информация рецептов', 'Рандомный рецепт', 'Информация ингредиентов']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)


def start(update: Update, _: CallbackContext):
    update.message.reply_text(
        "Ну и что ты тут сидишь, а блин?",
        reply_markup=markup,
    )

    return CHOOSING


def rec_info(update: Update, _: CallbackContext):
    text = update.message.text

    lang = detect_language(text)

    if lang != 'en':  # тут с помощью Api Яндекса определяется на каком языке написан запрос
        text = english_trans(text)

    recipe = search_recipes(text)

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

    update.message.reply_text(text_ing)
    update.message.reply_text(recipe_text)

    return CHOOSING


def ran_recipe(update: Update, _: CallbackContext) -> int:
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

    update.message.reply_text(text_ing)
    update.message.reply_text(recipe_text)

    return CHOOSING


def cancel(update: Update, _: CallbackContext) -> int:
    pass


def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CHOOSING: [
                MessageHandler(Filters.text & ~(Filters.command | Filters.regex('^Информация рецептов')), rec_info),
                MessageHandler(Filters.regex('^Рандомный рецепт$'), ran_recipe)]
        },
        fallbacks=[CommandHandler('cancel', cancel)],

    )

    # reply_keyboard = [['Информация рецептов', 'Рандомный рецепт', 'Информация ингредиентов']]

    dispatcher.add_handler(conv_handler)

    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TOKEN)
    updater.bot.setWebhook('https://food-project-lyceum.herokuapp.com/' +
                           TOKEN)

    updater.idle()


@app.route('/')
def index():
    return 'надпись'


if __name__ == '__main__':
    db_session.global_init('db/food_system.sqlite')
    PORT = int(os.environ.get("PORT", 5000))
    TOKEN = '1554384456:AAG_ZH5_8SLCPdxR2XfN5lKhDS16cFFACFI'
    main()
    app.run(host='0.0.0.0', port=PORT)
