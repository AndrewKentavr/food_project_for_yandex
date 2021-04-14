import parser

from . import db_session
from .search_history import SearchData
from flask import abort, jsonify
from flask_restful import Resource


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
        return jsonify({'history': search_history.to_dict(
            only=('id', 'search', 'user.id'))})

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
            only=('id', 'search', 'user.id')) for item in histories]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        search_history = SearchData(
            search=args['search'],
        )
        session.add(search_history)
        session.commit()
        return jsonify({'success': 'OK'})
