from flask import request
from flask_restful import Resource
from models import db, Category, CategorySchema


categories_schema = CategorySchema(many=True)
category_schema = CategorySchema()

class AddCategoryResource(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = category_schema.load(json_data)
        if errors:
            return errors, 422
            
        category = Category.query.filter_by(Name = json_data['Name']).first()
        if category is not None:
            return {'message': 'Category already exists'}, 409
 
        else:
            category = Category(
                Name=json_data['Name'])
                
            try:
                db.session.add(category)
                db.session.commit()
                return {
                    'message': 'Category {} was created'.format(json_data['Name']),
                    }
            except:
                return {'message': 'Something went wrong'}, 500