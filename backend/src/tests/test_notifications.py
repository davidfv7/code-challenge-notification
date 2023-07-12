from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_create_message():
    response = client.post("/messages", json={"message": "testmessage", "category": "Sports"})
    assert response.status_code == 201
    res = response.json()
    assert "message" in res
    assert "id" in res["message"]


def test_create_message_fail_if_parameter_is_missing():
    response = client.post("/messages", json={"category": "Sports"})
    res = response.json()
    assert response.status_code == 422
    assert "detail" in res


def test_get_notifications():
    response = client.get("/notifications",)
    assert response.status_code == 200
    res = response.json()
    assert "records" in res
    assert "total" in res

def test_get_notifications_with_correct_size():
    response = client.get("/notifications?page=1&size=5",)
    assert response.status_code == 200
    res = response.json()
    assert "records" in res
    assert len(res["records"]) <= 5

def test_get_notifications_fail_on_invalid_params():
    response = client.get("/notifications?page=page&size=size",)
    assert response.status_code == 422