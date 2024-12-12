# Creating APIs with Flask

## Overview
APIs (Application Programming Interfaces) allow applications to communicate with each other. Flask provides tools to build RESTful APIs that handle HTTP requests and return structured responses, such as JSON.

---

## Subtopic 1: Introduction to REST APIs

### Key Concepts
1. **What is a REST API?**
   - REST (Representational State Transfer) is an architectural style for designing networked applications.
   - Uses standard HTTP methods: `GET`, `POST`, `PUT`, `DELETE`.

2. **Benefits of REST APIs**:
   - Stateless and scalable.
   - Language-independent.
   - Easy to integrate with frontend applications.

3. **Key Components**:
   - **Endpoints**: URLs representing resources.
   - **HTTP Methods**: Define actions on resources.
   - **Responses**: Typically in JSON format.

---

## Subtopic 2: Setting Up Flask for API Development

### Key Concepts
1. **Flask and JSON Responses**:
   - Flask simplifies JSON response handling using `jsonify`.
   - Example:
     ```python
     from flask import jsonify

     @app.route("/api/data")
     def get_data():
         return jsonify({"message": "Hello, API!"})
     ```

2. **Installing Flask Extensions**:
   - Use `Flask-RESTful` for a structured API framework:
     ```bash
     pip install flask-restful
     ```

3. **Creating an API Class**:
```
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Define the API resource
class HelloWorld(Resource):
    def get(self):
        return {"message": "Hello, World"}

# Add the resource to the API with a specific endpoint
api.add_resource(HelloWorld, '/hello')

if __name__ == '__main__':
    app.run(debug=True)

```

```
python app.py
curl http://127.0.0.1:5000/hello
```

---

## Subtopic 3: Building RESTful Endpoints

### Key Concepts
1. **GET Method**:
   - Used to retrieve data:
     ```python
     @app.route("/items")
     def get_items():
         return jsonify(items)
     ```

2. **POST Method**:
   - Used to create new resources:
     ```python
     @app.route("/items", methods=["POST"])
     def add_item():
         data = request.json
         items.append(data)
         return jsonify(data), 201
     ```

3. **PUT and DELETE Methods**:
   - Update or delete resources by ID:
     ```python
     @app.route("/items/<int:item_id>", methods=["PUT"])
     def update_item(item_id):
         data = request.json
         items[item_id] = data
         return jsonify(data)

     @app.route("/items/<int:item_id>", methods=["DELETE"])
     def delete_item(item_id):
         del items[item_id]
         return '', 204
     ```

---


## Subtopic 5: Testing APIs

### Key Concepts
1. **Using Postman**:
   - Postman is a popular tool for testing RESTful APIs.
   - Create requests to test endpoints, passing parameters, headers, and JSON payloads.

2. **Using Curl**:
   - Command-line tool to test API endpoints:
     ```bash
     curl -X GET http://127.0.0.1:5000/
     ```
---
