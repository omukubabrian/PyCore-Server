

import sys
from  pathlib import Path

import pytest
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


import app as server
@pytest.fixture
def client():
    # Reset the temporary data before each test
    server.students = [
        {"id": 1, "name": "Brian", "course": "Computer science"},
        {"id": 2, "name": "Benita", "course": "Information Technology"}
    ]
    server.next_student_id = 3

    server.app.config["TESTING"] = True

    with server.app.test_client() as test_client:
        yield test_client


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
