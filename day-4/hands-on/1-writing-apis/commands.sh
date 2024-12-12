python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
pip install -r requirements.txt
python app.py


## Test
Use a browser, Postman, or curl to test the endpoints:
GET /hello: Returns {"message": "Hello, World"}.
GET /items: Returns the list of items.
POST /items: Creates a new item (JSON payload required: {"name": "item_name"}).
GET /items/<item_id>: Retrieves a specific item by ID.
PUT /items/<item_id>: Updates a specific item (JSON payload required).
DELETE /items/<item_id>: Deletes a specific item by ID.