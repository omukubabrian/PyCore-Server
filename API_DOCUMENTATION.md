
# PyCore Server API Documentation

## 1. Overview

PyCore Server is a student management REST API built using Python, Flask, and MySQL.

The API allows clients to create, retrieve, update, and delete student records.

### Technologies

- Python
- Flask
- MySQL
- JSON
- HTTP

## 2. Base URL

During local development:

http://127.0.0.1:5000

The base URL may change when the application is deployed.

## 3. Response Format

The API uses JSON for data exchange.

Clients should send JSON when an endpoint requires a request body and should expect JSON responses where implemented.

## 4. API Endpoints

### 4.1 Home

- **Method:** GET
- **Endpoint:** `/`
- **Purpose:** Access the API home route.

### 4.2 Health Check

- **Method:** GET
- **Endpoint:** `/health`
- **Purpose:** Check whether the API is responding.

### 4.3 Retrieve All Students

- **Method:** GET
- **Endpoint:** `/api/students`
- **Purpose:** Retrieve student records from the database.

### 4.4 Create a Student

- **Method:** POST
- **Endpoint:** `/api/students`
- **Purpose:** Add a new student record.

Example request body:

```json
{
  "name": "Brian",
  "course": "Computer Science"
}
```

The request requires a student name and course.

### 4.5 Retrieve One Student

- **Method:** GET
- **Endpoint:** `/api/students/<student_id>`
- **Purpose:** Retrieve one student using their ID.

Example:

`GET /api/students/1`

Replace `1` with the required student ID.

### 4.6 Update a Student

- **Method:** PUT
- **Endpoint:** `/api/students/<student_id>`
- **Purpose:** Update an existing student record.

Example request body:

```json
{
  "name": "Brian",
  "course": "Software Engineering"
}
```

Replace the example values with the details to be updated.

### 4.7 Delete a Student

- **Method:** DELETE
- **Endpoint:** `/api/students/<student_id>`
- **Purpose:** Delete a student record using its ID.

Example:

`DELETE /api/students/1`

Use the actual ID of the student to be deleted.

## 5. HTTP Status Codes

The following status codes are relevant to this API. Confirm the exact status returned by each route in the implementation.

| Status | Meaning |
|---|---|
| 200 | Request successful |
| 201 | Resource created |
| 400 | Invalid request |
| 404 | Resource not found |
| 500 | Unexpected server error |

## 6. Error Handling

The backend includes input validation and error handling.

Clients should check the HTTP status code and response body to determine whether a request succeeded.

Unexpected server errors should not expose database credentials or internal technical details to clients.

## 7. Testing

The API can be tested using:

- The frontend dashboard
- A browser for suitable GET requests
- VS Code terminal tools such as curl
- Automated tests using pytest

## 8. Database

The API uses MySQL to store student records.

The students table includes:

- `id` — automatically generated student identifier
- `name` — student's name
- `course` — student's course

## 9. Deployment

The local base URL is intended for development.

After deployment, update this documentation with the production API URL and verify the documented endpoints, response formats, and status codes against the deployed application.

## 10. Maintenance

Update this document whenever an endpoint, request format, response, or error-handling behavior changes.
