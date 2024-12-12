import requests

def list_all_items():
   # Define the API endpoint
  url = "http://127.0.0.1:5000/items"

  # Send a GET request
  response = requests.get(url)

  # Check the response status
  if response.status_code == 200:
      data = response.json()
      print("Data fetched successfully:", data)
  else:
      print(f"Failed to fetch data. Status code: {response.status_code}")


def item_add():
  # Define the API endpoint
  url = "http://127.0.0.1:5000/items"

  # Define the payload
  payload = {"name": "New Item"}

  # Send a POST request
  response = requests.post(url, json=payload)

  # Check the response status
  if response.status_code == 201:
      data = response.json()
      print("Item created successfully:", data)
  else:
      print(f"Failed to create item. Status code: {response.status_code}")

def update_item():
   # Define the API endpoint
   url = "http://127.0.0.1:5000/items/0"

   # Define the payload
   payload = {"name": "Updated Item"}

   # Send a PUT request
   response = requests.put(url, json=payload)

   # Check the response status
   if response.status_code == 200:
       data = response.json()
       print("Item updated successfully:", data)
   else:
       print(f"Failed to update item. Status code: {response.status_code}")

item_add()

update_item()

list_all_items()