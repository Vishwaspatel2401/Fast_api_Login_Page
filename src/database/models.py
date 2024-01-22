# database/models.py

# Add models related to SQL Alchemy

from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str