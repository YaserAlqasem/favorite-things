from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class Category(db.Model):
    __tablename__ = 'Category'
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(150), unique=True, nullable=False)

    def __init__(self, Name):
        self.Name = Name


class CategorySchema(ma.Schema):
    id = fields.Integer()
    Name = fields.String(required=True)
