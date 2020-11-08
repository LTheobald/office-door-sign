from project.app import app
from flask import json


def test_switch():
    tester = app.test_client()

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
    tester = app.test_client()
    response = tester.post("/status", content_type="application/json")

    assert response.status_code == 200
