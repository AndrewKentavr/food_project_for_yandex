import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import orm
from data.db_session import SqlAlchemyBase
from werkzeug.security import generate_password_hash, check_password_hash


class User(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    nick_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=True)
    password = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    search_history = orm.relation("SearchHistory", back_populates='user')
    calories_history = orm.relation("CaloriesHistory", back_populates='user')

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
