from flask import Flask, jsonify

app = Flask(__name__)

stores = [
    {
        'name': 'My Wondersul Store',
        'items': [
            {   
                'name': 'My Item',
                'price': 15.99
            }            
        ]
    }
]

@app.route('/store', methods=['POST'])
def create_store():
    pass

@app.route('/store/<string:name>')
def get_store(name):
    pass

@app.route('/store')
def get_stores():
    return jsonify({'sotores': stores})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass

@app.route('/store/<string:name>/item')
def get_intem_in_store(name):
    pass

