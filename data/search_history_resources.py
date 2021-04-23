import json
import parser

from flask import abort, jsonify, request
from flask_restful import Resource

from . import db_session
from .search_history import SearchData


def abort_if_history_not_found(history_id):
    session = db_session.create_session()
    search_history = session.query(SearchData).get(history_id)
    if not search_history:
        abort(404, message=f"history {history_id} not found")


class SearchHistoryResource(Resource):
    def get(self, history_id):
        abort_if_history_not_found(history_id)
        session = db_session.create_session()
        search_history = session.query(SearchData).get(history_id)
        return jsonify({'searches': search_history.to_dict(
            only=('id', 'history', 'user_id'))})

    def put(self, history_id):
        abort_if_history_not_found(history_id)

        session = db_session.create_session()
        search_history = session.query(SearchData).get(history_id)

        history = json.loads(search_history.history)
        if request.json['title'] in [element[0] for element in history]:
            history.pop(history.index(request.json['title']))
        history.append((request.json['title'], request.json['date']))
        print(history)

        search_history.history = json.dumps(history)
        session.commit()
        session.close()
        return jsonify({'success': 'OK'})

    def delete(self, history_id):
        abort_if_history_not_found(history_id)
        session = db_session.create_session()
        search_history = session.query().get(history_id)
        session.delete(search_history)
        session.commit()
        return jsonify({'success': 'OK'})


class SearchHistoryListResource(Resource):
    def get(self):
        session = db_session.create_session()
        histories = session.query(SearchData).all()
        return jsonify({'histories': [item.to_dict(
            only=('id', 'history', 'user_id')) for item in histories]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        search_history = SearchData(
            search=args['history'],
        )
        session.add(search_history)
        session.commit()
        return jsonify({'success': 'OK'})
