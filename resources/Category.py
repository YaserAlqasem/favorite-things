from flask import request
from flask_restful import Resource
from Model import db, Category, CategorySchema


categories_schema = CategorySchema(many=True)
category_schema = CategorySchema()