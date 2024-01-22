from database.models import User
from repos.users import DbUserRepo

user_repo = DbUserRepo(User)
