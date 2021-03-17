from security import identity
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import aunthenticate, identity

app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, aunthenticate, identity)

items = []

class Item(Resource):
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404
    
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
    
    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'item deleted'}
    
    def put(self,name):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'price',
            type = float,
            required = True,
            help = "this field cannot be left blank!"
        )
        data = request.get_json()
        
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item

class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')