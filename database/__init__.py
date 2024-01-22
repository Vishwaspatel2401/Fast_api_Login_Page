# database/__init__.py
from peewee import MySQLDatabase

db = MySQLDatabase(
    'myfirstdatabase',
    user='root',
    password='P@ssw0rd@123',
    host='127.0.0.1'
)


