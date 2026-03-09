from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class ScanResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    target = db.Column(db.String(100))
    ip = db.Column(db.String(100))
    port = db.Column(db.Integer)
    service = db.Column(db.String(100))
    risk = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
