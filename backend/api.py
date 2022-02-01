from flask import Blueprint
from flask_restful import Api, Resource
from models import get_all

api_bp = Blueprint('api', __name__, url_prefix='/api')

class Account(Resource):
    def get(self):
        return [{'id': x.id, 'name': x.name} for x in get_all()]

class Hoge(Resource):
    def get(self):
        return {'hoge': 'uga'}

api = Api(api_bp)
api.add_resource(Account, '/account')
api.add_resource(Hoge, '/hoge')