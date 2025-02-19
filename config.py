import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:2003@localhost:5432/testDB'
    SQLALCHEMY_TRACK_MODIFICATIONS = False