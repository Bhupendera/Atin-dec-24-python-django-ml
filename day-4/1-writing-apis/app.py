# File: app.py

from flask import Flask, request
from flask_restful import Api, Resource, abort

app = Flask(__name__)
api = Api(app)

# In-memory data store
items = []

# Error handling function
def abort_if_item_not_found(item_id):
    if item_id >= len(items) or item_id < 0:
        abort(404, message=f"Item {item_id} doesn't exist")

# API Resources
class HelloWorld(Resource):
    def get(self):
        return {"message": "Hello, World"}

class ItemList(Resource):
    def get(self):
        return items  # Return the items list directly

    def post(self):
        data = request.json
        if "name" not in data:
            return {"error": "Name is required"}, 400
        items.append(data)
        return data, 201

class Item(Resource):
    def get(self, item_id):
        abort_if_item_not_found(item_id)
        return items[item_id]  # Return the specific item

    def put(self, item_id):
        abort_if_item_not_found(item_id)
        data = request.json
        items[item_id] = data
        return data

    def delete(self, item_id):
        print(item_id)
        print(items)
        abort_if_item_not_found(item_id)
        del items[item_id]
        return '', 204

# Register API endpoints
api.add_resource(HelloWorld, '/hello')
api.add_resource(ItemList, '/items')
api.add_resource(Item, '/items/<int:item_id>')

if __name__ == '__main__':
    app.run(debug=True)
