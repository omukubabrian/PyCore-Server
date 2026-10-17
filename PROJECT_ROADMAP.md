
# PyCore Server — Project Roadmap

## Project Overview

PyCore Server is a student management application built with Python, Flask, MySQL, HTML, CSS, and JavaScript.

The project aims to develop a working web application while learning how the frontend, backend, and database communicate.

## Phase 1: Environment and Project Setup

-  Install Python and Git
-  Set up VS Code
-  Create the project folder
- Create and activate a Python virtual environment
-  Install Flask
-  Create app.py
- Create .gitignore
- Create README.md
- Initialize Git and make the first commit

## Phase 2: Flask API Development

-  Create the Flask application
-  Create the home route
- Create the health-check endpoint
- [x] Implement GET all students
- [x] Implement POST a new student
- [x] Implement GET one student by ID
- [x] Implement PUT to update a student
- [x] Implement DELETE a student
- [x] Add input validation
- [x] Add error handling
- [x] Write automated tests
- [x] Confirm that seven tests passed

## Phase 3: Git and GitHub

- [x] Create a GitHub repository
- [x] Connect the local project to GitHub
- [x] Push the project to the main branch
- [x] Commit and push subsequent changes
- [x] Configure .gitignore to protect sensitive files

## Phase 4: MySQL Database Integration

- [x] Install MySQL Server
- [x] Set up MySQL Workbench
- [x] Create the pycore database
- [x] Create the students table
- [x] Configure database user permissions
- [x] Store database configuration in .env
- [x] Create database.py
- [x] Connect Flask to MySQL
- [x] Implement database CRUD operations
- [x] Add database error handling
- [x] Create the pycore_test database

## Phase 5: Frontend Development

- [x] Create the frontend folder
- [x] Create index.html
- [x] Create style.css
- [x] Create script.js
- [x] Design the student dashboard
- [x] Display student records in a table
- [x] Display total students and server status
- [x] Create the Add Student form
- [x] Implement Edit and Delete actions
- [x] Use JavaScript fetch() to call the API
- [x] Configure the backend API URL
- [x] Configure Flask-CORS
- [x] Run the frontend using VS Code Live Server

## Phase 6: Understand Frontend and Backend Communication

- [x] Understand the roles of HTML, CSS, and JavaScript
- [x] Understand the role of Flask
- [x] Understand the role of MySQL
- [x] Understand the request-response cycle
- [x] Understand the frontend and backend ports
- [x] Understand why CORS is needed
- [x] Learn the GET, POST, PUT, and DELETE methods
- [x] Learn basic HTTP status codes
- [x] Understand Flask routes and URL parameters
- [ ] Complete the lesson on async and await
- [ ] Understand JSON requests and responses
- [ ] Understand JavaScript promises
- [ ] Trace a request through the entire application

## Phase 7: Understand the Existing JavaScript

- [ ] Understand API_URL
- [ ] Understand the apiRequest() function
- [ ] Understand template literals
- [ ] Understand fetch() and its options
- [ ] Understand HTTP request headers
- [ ] Understand response.json()
- [ ] Understand response.ok
- [ ] Understand error handling with try and catch
- [ ] Understand checkServer()
- [ ] Understand loadStudents()
- [ ] Understand how JavaScript displays student records
- [ ] Understand form submission
- [ ] Understand how the Edit operation works
- [ ] Understand how the Delete operation works
- [ ] Understand event listeners and DOM manipulation


## Phase 8: Test the Complete Application

- [ ] Start and verify MySQL
- [ ] Start the Flask backend
- [ ] Open the frontend using Live Server
- [ ] Verify the server status
- [ ] Add a student and verify it in MySQL
- [ ] Refresh the page and verify data persistence
- [ ] Edit a student
- [ ] Delete a student
- [ ] Test invalid input
- [ ] Test nonexistent student IDs
- [ ] Inspect browser developer tools
- [ ] Inspect Flask logs
- [ ] Run the automated tests again

## Phase 9: Security and Code Quality

- [ ] Verify that .env is excluded from Git
- [ ] Use parameterized SQL queries
- [ ] Validate input on the backend
- [ ] Return appropriate HTTP status codes
- [ ] Avoid exposing sensitive information in errors
- [ ] Check database connection and cursor cleanup
- [ ] Review the project structure
- [ ] Improve automated test coverage
- [ ] Document the API endpoints

## Phase 10: Deployment

- [ ] Understand local development versus production
- [ ] Choose a hosting platform
- [ ] Configure production environment variables
- [ ] Deploy the Flask API
- [ ] Set up an accessible production MySQL database
- [ ] Configure secure database access
- [ ] Update the frontend API URL
- [ ] Configure production CORS
- [ ] Deploy the frontend
- [ ] Test the live application
- [ ] Verify all CRUD operations online
- [ ] Document the deployment process

## Phase 11: Final GitHub Documentation

- [ ] Commit the final changes
- [ ] Push the completed project to GitHub
- [ ] Update README.md with project details
- [ ] Document installation and setup instructions
- [ ] Document API endpoints and examples
- [ ] Add dashboard screenshots
- [ ] Add the live demo link after deployment
- [ ] Check that no passwords or secrets are exposed

## Final Project Goals

- [ ] Explain how the frontend communicates with Flask
- [ ] Explain how Flask communicates with MySQL
- [ ] Demonstrate all CRUD operations
- [ ] Pass the automated tests
- [ ] Deploy a working application
- [ ] Maintain complete project documentation



Current focus: Learn the existing JavaScript step by step before moving to final testing and deployment.
