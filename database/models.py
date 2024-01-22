# database/models.py
from peewee import Model, CharField
from . import db  


class User(Model):
    username = CharField(unique=True)
    password = CharField() 

    class Meta:
        database = db  
        table_name = "users" 
        
