from flask import abort, jsonify, request
from flask_restful import Resource

from data.search_history import SearchData
from . import db_session
from .users import User


def abort_if_user_not_found(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404, message=f"User {user_id} not found")


class UserResource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        return jsonify({'user': user.to_dict(
            only=('id', 'nick_name', 'email'))})

    def delete(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})


class UserListResource(Resource):
    def get(self):
        session = db_session.create_session()
        news = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('nick_name', 'email', 'id')) for item in news]})

    def post(self):
        session = db_session.create_session()

        user = User(email=request.json['email'], nick_name=request.json['nick_name'])
        user.set_password(request.json['password'])
        session.add(user)
        session.commit()

        search_history = SearchData(user_id=user.id, history='[]')
        session.add(search_history)
        session.commit()

        return jsonify({'success': f'{user.id}'})
