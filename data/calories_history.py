import sqlalchemy
from datetime import date
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import orm
from data.db_session import SqlAlchemyBase


class CaloriesData(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'calories_history'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    calories = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    
    date = sqlalchemy.Column(sqlalchemy.Date, default=date.today())
    user = orm.relationship('User', backref="calories")
