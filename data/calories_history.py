import sqlalchemy
from datetime import date

from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import orm
from data.db_session import SqlAlchemyBase


class CaloriesData(SqlAlchemyBase, SerializerMixin, UserMixin):
    __tablename__ = 'calories_history'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    calories = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

    date = sqlalchemy.Column(sqlalchemy.Date, default=date.today())
    user = orm.relation('User')
