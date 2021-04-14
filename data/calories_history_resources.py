import parser

from . import db_session
from .calories_history import CaloriesData
from flask import abort, jsonify
from flask_restful import Resource


def abort_if_history_not_found(history_id):
    session = db_session.create_session()
    search_history = session.query(CaloriesData).get(history_id)
    if not search_history:
        abort(404, message=f"history {history_id} not found")


class CaloriesHistoryResource(Resource):
    def get(self, history_id):
        abort_if_history_not_found(history_id)
        session = db_session.create_session()
        calories_history = session.query(CaloriesData).get(history_id)
        return jsonify({'history': calories_history.to_dict(
            only=('id', 'calories', 'user.id', 'date'))})

    def delete(self, history_id):
        abort_if_history_not_found(history_id)
        session = db_session.create_session()
        search_history = session.query().get(history_id)
        session.delete(search_history)
        session.commit()
        return jsonify({'success': 'OK'})


class CaloriesHistoryListResource(Resource):
    def get(self):
        session = db_session.create_session()
        histories = session.query(CaloriesData).all()
        return jsonify({'histories': [item.to_dict(
            only=('id', 'calories', 'user.id', 'date')) for item in histories]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        calories_history = CaloriesData(
            search=args['calories'],
        )
        session.add(calories_history)
        session.commit()
        return jsonify({'success': 'OK'})
