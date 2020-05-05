from flask import request
from flask_restful import Resource
from models import db, Item, ItemSchema


items_schema = ItemSchema(many=True)
item_schema = ItemSchema()