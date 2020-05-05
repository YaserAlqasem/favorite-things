from flask import Blueprint
from flask_restful import Api
from resources.Category import AddCategoryResource,CategoriesListResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(AddCategoryResource, '/AddCategory')
api.add_resource(CategoriesListResource, '/Categories')