from project.app import app
from flask import json

tester = app.test_client()


def test_root():
    response = tester.get("/")
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data["running"]


def test_switch():
    # Posting with a state of 'off' will turn the display off
    response = tester.post("/switch", json={"switch":"off"}, content_type="application/json")
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data["switch"] == "off"

    # Posting with a state of 'on' will turn the display on
    response = tester.post("/switch", json={"switch":"on"}, content_type="application/json")
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data["switch"] == "on"

    # Posting with no body will cause an error
    response = tester.post("/switch", content_type="application/json")
    assert response.status_code == 400

    # Posting with a state of 'unknown' will return an error (as that state is unknown)
    response = tester.post("/switch", data=dict(switch="unknown"), content_type="application/json")
    assert response.status_code == 400


def test_status():
    response = tester.post("/status", content_type="application/json")

    # Posting with a status of free will set the free status on
    response = tester.post("/status", json={"status":"free"}, content_type="application/json")
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data["status"] == "free"

    # Posting with a status of working will set the free status on
    response = tester.post("/status", json={"status":"working"}, content_type="application/json")
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data["status"] == "working"

    # Posting with a status of oncall will set the free status on
    response = tester.post("/status", json={"status":"on_call"}, content_type="application/json")
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data["status"] == "on_call"

    # Posting an unknown status returns a 404
    response = tester.post("/status", json={"status":"somethingmadeup"}, content_type="application/json")
    assert response.status_code == 404
