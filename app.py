from flask import Blueprint
from flask_restful import Api
from resources.Category import AddCategoryResource,CategoriesListResource,EditCategoryResource,DeleteCategoryResource
from resources.Item import AddItemResource,ItemsListResource,EditItemResource,DeleteItemResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(AddCategoryResource, '/AddCategory')
api.add_resource(CategoriesListResource, '/Categories')
api.add_resource(EditCategoryResource, '/EditCategory/<categoryid>')
api.add_resource(DeleteCategoryResource, '/DeleteCategory/<categoryid>')

api.add_resource(AddItemResource, '/AddItem')
api.add_resource(ItemsListResource, '/Items')
api.add_resource(EditItemResource, '/EditItem/<itemid>')
api.add_resource(DeleteItemResource, '/DeleteItem/<itemid>')