import os

from flask import Flask
from flask_restful import Api

from data import db_session
from data import users_resources, search_history_resources

app = Flask(__name__)
api = Api(app)

api.add_resource(users_resources.UserListResource, '/api/users')
api.add_resource(users_resources.UserResource, '/api/users/<int:user_id>')
api.add_resource(search_history_resources.SearchHistoryListResource, '/api/search_histories')
api.add_resource(search_history_resources.SearchHistoryResource, '/api/search_histories/<int:history_id>')

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def index():
    return None


if __name__ == '__main__':
    db_session.global_init('db/food_system.sqlite')
    print(db_session.__factory)
    port = int(os.environ.get("PORT", 5000))
    app.run()