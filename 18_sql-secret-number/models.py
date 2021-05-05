import os
from sqla_wrapper import SQLAlchemy

db = SQLAlchemy(os.getenv("DATABASE_URL", "sqlite:///localhost.sqlite"))


class User(db.Model):
    username = db.Column(db.String, primary_key=True)
    secret_number = db.Column(db.Integer, unique=False)
