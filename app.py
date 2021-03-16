from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

items = []

class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {'item': None}, 404
    
    def post(self, name):
        item = {
            'name': name,
            'price': 12.00
        }
        items.append(item)
        return item, 201

class ItemList(Resource):
    def get(self):
        data = request.get_json(force=True)
        # Variables
        name = data['name']
        price = data['price']
        
        item = {
            'name': name,
            'price': price
        }
        items.append(item)
        return item, 201

api.add_resource(Item, '/item/<string:name>')