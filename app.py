from flask import Flask, jsonify, request

# create our Flask application
app = Flask(__name__)

# Temporary data stored in memory
students = [
    {"id": 1, "name": "Brian", "course": "Computer science"},
    {"id": 2, "name": "Benita", "course": "Information Technology"}
]

# Generating the next student ID
next_student_id = 3


# home endpoint: provides basic project information
@app.route("/", methods=["GET"])
def home():
    return (
        jsonify({
            "project": "PyCore Server",
            "message": "Our python server is running!",
            "status": "success",
        }),
        200,
    )


# Health endpoint: checks whether the server is responding
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200


# GET: retrieve all students
@app.route("/api/students", methods=["GET"])
def get_students():
    return (
        jsonify({"count": len(students), "students": students}),
        200,
    )


# POST: create a new student
@app.route("/api/students", methods=["POST"])
def create_students():
    global next_student_id

    # read the incoming JSON request body
    data = request.get_json(silent=True)

    # Reject requests without a valid JSON object
    if not isinstance(data, dict):
        return (
            jsonify({"error": "Request body must be a JSON object."}),
            400,
        )

    # read and validate the required fields
    name = data.get("name")
    course = data.get("course")

    if not isinstance(name, str) or not name.strip():
        return (
            jsonify({"error": "A non-empty name is required."}),
            400,
        )

    if not isinstance(course, str) or not course.strip():
        return (
            jsonify({"error": "A non-empty course is required."}),
            400,
        )

    # create student record
    student = {
        "id": next_student_id,
        "name": name.strip(),
        "course": course.strip(),
    }
    # save it in our temporary list
    students.append(student)
    next_student_id += 1

    # Return the created record with HTTP status 201
    return (
        jsonify({
            "message": "Student created successfully.",
            "student": student,
        }),
        201,
    )


# Run the development server
if __name__ == "__main__":
    app.run(
        host="127.0.0.1", 
        port=5000, 
        debug=True
        )