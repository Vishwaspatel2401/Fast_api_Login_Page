from typing import List
from database.models import User

class UserRepo:
    def get_user_by_username(self, username: str):
        pass

    def create_user(self, username: str, password: str):
        pass

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
        pass

    def create_user(self, username: str, password: str):
        pass

