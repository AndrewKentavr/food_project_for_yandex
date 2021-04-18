import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import orm
from data.db_session import SqlAlchemyBase


class SearchData(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'search_history'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    history = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    user = orm.relationship('User', backref="searches")
