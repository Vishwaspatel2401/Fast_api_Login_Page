from fastapi import APIRouter, HTTPException, status , Depends
from dependency_injector.wiring import Provide, inject

from container import Container
from entities.user_entities import UserCredentials
from repos import user_repo
from passlib.context import CryptContext

from repos.users import UserRepo


router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@inject
def get_session_token(credentials: UserCredentials, user_repo: UserRepo = Depends(Provide[Container.user_repo])):
    username = credentials.username
    password = credentials.password

    user = user_repo.get_user_by_username(username)

    print(user)
    
    if user and pwd_context.verify(password, user.password):
        return f"session_token_for_{username}"
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )


@inject
def get_current_user(token: str, user_repo: UserRepo = Depends(Provide[Container.user_repo])):
    username = token.split("_")[-1]
    user = user_repo.get_user_by_username(username)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid session token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


@router.post("/register")
@inject
async def register(user: UserCredentials, user_repo: UserRepo = Depends(Provide[Container.user_repo])):   
    try:
        existing_user = user_repo.get_user_by_username(user.username)
    except ValueError:
        existing_user = False

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this username already exists",
        )
 
    hashed_password = pwd_context.hash(user.password)
    created_user = user_repo.create_user(user.username, hashed_password)

    return {"username": created_user.username}


@router.post("/login")
@inject
async def login(credentials: UserCredentials, user_repo: UserRepo = Depends(Provide[Container.user_repo])):
    token = get_session_token(credentials)
    return {"session_token": token}


@router.post("/logout")
@inject
async def logout():
    return {"message": "Logout successful"}


