from flask import Flask, jsonify, request

# Create our Flask application
app = Flask(__name__)

# Temporary data stored in memory
students = [
    {"id": 1, "name": "Brian", "course": "Computer science"},
    {"id": 2, "name": "Benita", "course": "Information Technology"}
]

# Generate the next student ID
next_student_id = 3


# HOME ENDPOINT: Provide basic project information
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "project": "PyCore Server",
        "message": "Our python server is running!",
        "status": "success"
    }), 200


# HEALTH ENDPOINT: Check whether the server is responding
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200


# GET: Retrieve all students
@app.route("/api/students", methods=["GET"])
def get_students():
    return jsonify({
        "count": len(students),
        "students": students
    }), 200


# POST: Create a new student
@app.route("/api/students", methods=["POST"])
def create_students():
    global next_student_id

    # Read the incoming JSON request body
    data = request.get_json(silent=True)

    # Reject requests without a valid JSON object
    if not isinstance(data, dict):
        return jsonify({
            "error": "Request body must be a JSON object."
        }), 400

    # Read and validate the required fields
    name = data.get("name")
    course = data.get("course")

    if not isinstance(name, str) or not name.strip():
        return jsonify({
            "error": "A non-empty name is required."
        }), 400

    if not isinstance(course, str) or not course.strip():
        return jsonify({
            "error": "A non-empty course is required."
        }), 400

    # Create the student record
    student = {
        "id": next_student_id,
        "name": name.strip(),
        "course": course.strip()
    }

    # Save the student in the temporary list
    students.append(student)
    next_student_id += 1

    # Return the created record with HTTP status 201
    return jsonify({
        "message": "Student created successfully.",
        "student": student
    }), 201


# GET: Retrieve one student using their ID
@app.route("/api/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return jsonify({"student": student}), 200

    return jsonify({
        "error": "Student not found."
    }), 404


# PUT: Update an existing student
@app.route("/api/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    # Read the incoming JSON request body
    data = request.get_json(silent=True)

    # Validate the request body
    if not isinstance(data, dict):
        return jsonify({
            "error": "Request body must be a JSON object."
        }), 400

    name = data.get("name")
    course = data.get("course")

    # Validate the name
    if not isinstance(name, str) or not name.strip():
        return jsonify({
            "error": "A non-empty name is required."
        }), 400

    # Validate the course
    if not isinstance(course, str) or not course.strip():
        return jsonify({
            "error": "A non-empty course is required."
        }), 400

    # Find and update the requested student
    for student in students:
        if student["id"] == student_id:
            student["name"] = name.strip()
            student["course"] = course.strip()

            return jsonify({
                "message": "Student updated successfully.",
                "student": student
            }), 200

    # Return an error if the student does not exist
    return jsonify({
        "error": "Student not found."
    }), 404


# DELETE: Remove a student using their ID
@app.route("/api/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    # Find the student's position in the list
    for index, student in enumerate(students):
        if student["id"] == student_id:
            # Remove the student and keep the deleted record
            deleted_student = students.pop(index)

            return jsonify({
                "message": "Student deleted successfully.",
                "student": deleted_student
            }), 200

    # Return an error if the student does not exist
    return jsonify({
        "error": "Student not found."
    }), 404


# Run the development server
if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )