# Consuming a Flask API from Python

## Overview
Flask APIs can be easily consumed using Python, thanks to libraries like `requests`. This document outlines how to interact with Flask APIs by sending requests and handling responses.

---

## Prerequisites
1. **Python Installed**: Ensure Python 3.7+ is installed on your machine.
2. **Install Required Library**:
   ```bash
   pip install requests
   ```
3. **Run Flask API**: Make sure the Flask API you want to consume is running and accessible.

---

## Steps to Consume a Flask API

### 1. Import the `requests` Library
The `requests` library simplifies HTTP operations like GET, POST, PUT, and DELETE.

### 2. Send HTTP Requests
Use the appropriate HTTP method for the operation you want to perform (e.g., retrieve, create, update, or delete data).

### 3. Handle API Responses
Flask APIs typically return JSON responses. Use the `.json()` method to parse the response data into Python dictionaries or lists.

### 4. Example Code for Common Operations

#### **GET Request**: Fetch Data
```python
import requests

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
```

#### **POST Request**: Create a New Resource
```python
import requests

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
```

#### **PUT Request**: Update an Existing Resource
```python
import requests

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
```

#### **DELETE Request**: Remove a Resource
```python
import requests

# Define the API endpoint
url = "http://127.0.0.1:5000/items/0"

# Send a DELETE request
response = requests.delete(url)

# Check the response status
if response.status_code == 204:
    print("Item deleted successfully.")
else:
    print(f"Failed to delete item. Status code: {response.status_code}")
```

---

## Error Handling
It is important to handle potential errors when interacting with APIs. Common issues include:
1. **Invalid Endpoint**: Ensure the URL is correct.
2. **Network Issues**: Handle connection errors gracefully using `try-except` blocks.
3. **Non-200 Status Codes**: Check the status code and provide meaningful messages.

#### Example of Error Handling
```python
import requests

url = "http://127.0.0.1:5000/items"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an HTTPError for bad responses
    data = response.json()
    print("Data fetched successfully:", data)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
```

---

## Advanced Techniques

### 1. Passing Query Parameters
```python
params = {"key": "value"}
response = requests.get("http://127.0.0.1:5000/items", params=params)
print(response.json())
```

### 2. Sending Headers
```python
headers = {"Authorization": "Bearer token"}
response = requests.get("http://127.0.0.1:5000/items", headers=headers)
print(response.json())
```

### 3. Handling Large Responses
```python
response = requests.get("http://127.0.0.1:5000/large-items", stream=True)
for chunk in response.iter_content(chunk_size=1024):
    process(chunk)  # Replace with your logic
```

---

## Conclusion
Consuming a Flask API from Python is straightforward using the `requests` library. By sending HTTP requests, handling responses, and incorporating error management, you can efficiently interact with APIs in your Python applications