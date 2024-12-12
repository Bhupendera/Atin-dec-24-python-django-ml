# Test APIs with Tools and Scripts

## Overview
Testing APIs is a crucial step in ensuring their functionality, performance, and reliability. This hands-on guide demonstrates how to test APIs using tools and scripts.

---

## Tools for API Testing

### 1. Postman
Postman is a popular GUI tool for testing APIs, offering features like request creation, parameterization, and automation.

#### Steps to Test APIs with Postman:
1. **Install Postman**:
   - Download Postman from [postman.com/downloads](https://www.postman.com/downloads/).
   
2. **Create a New Request**:
   - Open Postman and click on **New** > **Request**.
   - Choose the method (e.g., `GET`, `POST`, `PUT`, `DELETE`).
   - Enter the API endpoint (e.g., `http://127.0.0.1:5000/items`).

3. **Set Headers**:
   - Add necessary headers (e.g., `Content-Type: application/json` for JSON APIs).

4. **Add Body Data** (for methods like `POST` or `PUT`):
   - Select **Body** and choose **raw**.
   - Add the JSON payload, e.g., `{ "name": "NewItem" }`.

5. **Send Request**:
   - Click **Send** to execute the request.
   - View the response in the bottom panel, including status code, response time, and data.

6. **Save Requests**:
   - Save the request to a collection for future use.

#### Example Test Scenario:
- Test `POST /items`:
  - Method: `POST`
  - URL: `http://127.0.0.1:5000/items`
  - Headers: `{ "Content-Type": "application/json" }`
  - Body: `{ "name": "Sample Item" }`

- Test `GET /items`:
  - Method: `GET`
  - URL: `http://127.0.0.1:5000/items`

### 2. Curl
Curl is a command-line tool for making HTTP requests.

#### Installing Curl:
- **Linux/Mac**: Pre-installed on most systems.
- **Windows**: Download from [curl.se](https://curl.se/).

#### Curl Commands:
1. **GET Request**:
   ```bash
   curl -X GET http://127.0.0.1:5000/items
   ```

2. **POST Request**:
   ```bash
   curl -X POST http://127.0.0.1:5000/items \
        -H "Content-Type: application/json" \
        -d '{"name": "Sample Item"}'
   ```

3. **PUT Request**:
   ```bash
   curl -X PUT http://127.0.0.1:5000/items/0 \
        -H "Content-Type: application/json" \
        -d '{"name": "Updated Item"}'
   ```

4. **DELETE Request**:
   ```bash
   curl -X DELETE http://127.0.0.1:5000/items/0
   ```

### 3. PowerShell
PowerShell can be used to send HTTP requests and is built into Windows systems.

#### PowerShell Commands:
1. **GET Request**:
   ```powershell
   Invoke-WebRequest -Uri "http://127.0.0.1:5000/items" -Method GET
   ```

2. **POST Request**:
   ```powershell
   $body = @{name="Sample Item"} | ConvertTo-Json
   Invoke-WebRequest -Uri "http://127.0.0.1:5000/items" -Method POST -Body $body -ContentType "application/json"
   ```

3. **PUT Request**:
   ```powershell
   $body = @{name="Updated Item"} | ConvertTo-Json
   Invoke-WebRequest -Uri "http://127.0.0.1:5000/items/0" -Method PUT -Body $body -ContentType "application/json"
   ```

4. **DELETE Request**:
   ```powershell
   Invoke-WebRequest -Uri "http://127.0.0.1:5000/items/0" -Method DELETE
   ```

---

## Conclusion
Using tools like Postman, Curl, PowerShell, you can effectively test APIs for functionality, performance, and error handling. Automating these tests ensures consistent and repeatable validation of your APIs.

