
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import app as server
from database import get_db_connection as real_get_db_connection


@pytest.fixture
def client():
    # Save the original database connection function.
    original_get_db_connection = server.get_db_connection

    # Redirect API database connections to the test database.
    server.get_db_connection = (
        lambda: real_get_db_connection("pycore_test")
    )
    server.app.config["TESTING"] = True

    try:
        # Prepare predictable records before each test.
        connection = real_get_db_connection("pycore_test")

        try:
            cursor = connection.cursor()

            try:
                cursor.execute("DELETE FROM students")

                cursor.execute(
                    """
                    INSERT INTO students (id, name, course)
                    VALUES
                        (1, 'Brian', 'Computer science'),
                        (2, 'Benita', 'Information Technology')
                    """
                )

                connection.commit()

            finally:
                cursor.close()

        finally:
            connection.close()

        # Create the Flask test client.
        with server.app.test_client() as test_client:
            yield test_client

    finally:
        # Restore the original connection function.
        server.get_db_connection = original_get_db_connection


def test_get_all_students(client):
    response = client.get("/api/students")

    assert response.status_code == 200
    assert response.json["count"] == 2


def test_get_one_student(client):
    response = client.get("/api/students/1")

    assert response.status_code == 200
    assert response.json["student"]["name"] == "Brian"


def test_create_student(client):
    response = client.post(
        "/api/students",
        json={"name": "Mary", "course": "Cybersecurity"}
    )

    assert response.status_code == 201
    assert response.json["student"]["name"] == "Mary"


def test_reject_invalid_student(client):
    response = client.post(
        "/api/students",
        json={"name": "", "course": "Cybersecurity"}
    )

    assert response.status_code == 400


def test_update_student(client):
    response = client.put(
        "/api/students/1",
        json={"name": "Brian", "course": "Software Engineering"}
    )

    assert response.status_code == 200
    assert response.json["student"]["course"] == "Software Engineering"


def test_delete_student(client):
    response = client.delete("/api/students/2")

    assert response.status_code == 200
    assert response.json["student"]["name"] == "Benita"


def test_student_not_found(client):
    response = client.get("/api/students/999")

    assert response.status_code == 404
    assert response.json["error"] == "Student not found."
