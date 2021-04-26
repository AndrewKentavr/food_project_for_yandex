import sqlalchemy
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin

from data.db_session import SqlAlchemyBase


# класс истории поиска для пользователя
# имеет свой id, саму историю в виде списка, преобразованного в строку,
# а также он имеет отношение к классу User через user_id
class SearchData(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'search_history'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    history = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    user = orm.relationship('User', backref="searches")
