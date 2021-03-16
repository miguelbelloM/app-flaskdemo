from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

items = []

class Item(Resource):
    def get(self, name):
        item = next(filter(lambda item: item['name'] == name, items), None)
        return {'item': item}, 200 if item is item else 404
    
    def post(self, name):
        if next(filter(lambda item: item['name'] == name, items), None) is not None:
            return {'message': "An item with name '{}' already exists".format(name)}, 400

        data = request.get_json()
        # Variables
        price = data['price']
        
        item = {
            'name': name,
            'price': price
        }
        items.append(item)
        return item, 201

class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')