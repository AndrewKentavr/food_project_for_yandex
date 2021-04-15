import sqlalchemy
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import orm
from data.db_session import SqlAlchemyBase


class SearchData(SqlAlchemyBase, SerializerMixin, UserMixin):
    __tablename__ = 'search_history'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    search = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    user = orm.relation('User')
