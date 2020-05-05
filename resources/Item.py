from flask import request
from flask_restful import Resource
from models import db, Item, ItemSchema


items_schema = ItemSchema(many=True)
item_schema = ItemSchema()

class AddItemResource(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = item_schema.load(json_data)
        if errors:
            return errors, 422
            
        item = Item.query.filter_by(Title = json_data['Title']).first()
        if item is not None:
            return {'message': 'Item already exists'}, 409
 
        else:
            item = Item(
                Title=json_data['Title'],
                Description = json_data['Description'],
                Ranking = json_data['Ranking'],
                Category_id = json_data['Category_id'])
                
            try:
                db.session.add(item)
                db.session.commit()
                return {
                    'message': 'Item {} was created'.format(json_data['Title']),
                    }
            except:
                return {'message': 'Something went wrong'}, 500