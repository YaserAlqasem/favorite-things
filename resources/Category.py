from flask import request
from flask_restful import Resource
from models import db, Category, CategorySchema,Log


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

                log = Log(
                    ActionName = request.path,
                    Message = category.Name + " Category has been Added")
                db.session.add(log)
                db.session.commit()    
                return {
                    'message': 'Category {} was created'.format(json_data['Name']),
                    }
            except:
                return {'message': 'Something went wrong'}, 500

class CategoriesListResource(Resource):
    def get(self):
        categories = Category.query.all()
        categories = categories_schema.dump(categories).data
        if categories:
            return {'status': 'success', 'data': categories}, 200
        else:
            return {'message': 'There is no categories found'}, 404

class EditCategoryResource(Resource):
    def post(self,categoryid):
        categoryData = request.get_json(force=True)
        category = Category.query.filter_by(id = categoryid).first()

        if category is not None:
            category.Name = categoryData['Name']
            log = Log(
                ActionName = request.path,
                Message = category.Name + " Category has been Edited")
            db.session.add(log)
            db.session.commit()
            return {'message': 'Category {} updated successfuly'.format(categoryData['Name'])}, 200
        else:
            return {'message': 'There is no Category found'}, 404

class DeleteCategoryResource(Resource):
    def post(self,categoryid):
        categoryData = request.get_json(force=True)
        category = Category.query.filter_by(id = categoryid).first()

        if category is not None:
            db.session.delete(category)
            log = Log(
                ActionName = request.path,
                Message = category.Name + " Category has been Deleted")
            db.session.add(log)
            db.session.commit()
            return {'message': 'Category {} deleted successfuly'.format(category.Name)}, 200
        else:
            return {'message': 'There is no Category found'}, 404