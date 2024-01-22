from pydantic import BaseModel


class UserCredentials(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    session_token: str


