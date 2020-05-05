from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
import datetime

ma = Marshmallow()
db = SQLAlchemy()


class Category(db.Model):
    __tablename__ = 'Category'
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(150), unique=True, nullable=False)
    
    
    item = relationship("Item", back_populates="category")

    def __init__(self, Name):
        self.Name = Name


class CategorySchema(ma.Schema):
    id = fields.Integer()
    Name = fields.String(required=True)


class Item(db.Model):
    __tablename__ = 'Item'
    id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(50), nullable=False)
    Description = db.Column(db.String(150), nullable=True)
    Ranking = db.Column(db.Integer, unique=True,nullable=True)
    Category_id = db.Column(db.Integer, db.ForeignKey(Category.id))
    CreatedDate = db.Column(db.DateTime, nullable=False)
    ModifiedDate = db.Column(db.DateTime, nullable=False)

    category = relationship('Category', back_populates="item")   

    def __init__(self, Title,Description,Ranking,Category_id):
        self.Title = Title
        self.Description = Description
        self.Ranking = Ranking
        self.Category_id = Category_id
        self.CreatedDate = datetime.datetime.now()
        self.ModifiedDate = datetime.datetime.now()

class ItemSchema(ma.Schema):
    id = fields.Integer()
    Title = fields.String(required=True)
    Description = fields.String(required=False)
    Ranking = fields.Integer(required=True)
    Category_id = fields.Integer(required=True)
    CreatedDate = fields.DateTime()
    ModifiedDate = fields.DateTime()