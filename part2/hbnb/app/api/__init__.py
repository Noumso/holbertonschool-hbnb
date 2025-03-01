from flask import Blueprint
from flask_restx import Api
from .v1.places import api as places_ns
# from .v1.amenities import api as amenities_ns
# from .v1.reviews import api as reviews_ns
from .v1.users import api as users_ns

# Initialize blueprint and API
blueprint = Blueprint('api', __name__)
api = Api(blueprint, title='HBnB API', version='1.0', description='API')

# Register namespaces
api.add_namespace(places_ns, path='/api/v1/places')
# api.add_namespace(amenities_ns, path='/api/v1/amenities')
# api.add_namespace(reviews_ns, path='/api/v1/reviews')
api.add_namespace(users_ns, path='/api/v1/users')
