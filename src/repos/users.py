from typing import List

from database.models import User
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from database.models import Base

class UserRepo:

    def __init__(self, db_uri: str):
        self.engine = create_engine(db_uri)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def get_user_by_username(self, username: str):
        session = self.Session()
        user = session.query(User).filter_by(username=username).first()
        session.close()

    def create_user(self, username: str, password: str):
        new_user = User(username=username, password=password)
        session = self.Session()
        session.add(new_user)
        
        session.commit()
        session.close()

class DbUserRepo(UserRepo):
    def __init__(self, model):
        self.model = model

    def get_user_by_username(self, username: str):
        return self.model.get_or_none(User.username == username)

    def create_user(self, username: str, password: str):
        return self.model.create(username=username, password=password)


class StaticUserRepo(UserRepo):
    def __init__(self):
        self.users: List[User] = [
            User(username="first", password="first"),
            User(username="second", password="second")
        ]

    def get_user_by_username(self, username: str):
        for u in self.users:
            if u.username == username:
                return u
        raise ValueError("User not found")

    def create_user(self, username: str, password: str):
        user = User(username=username, password=password)
        self.users.append(user)
        return user

