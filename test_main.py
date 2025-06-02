from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_reset():
    response = client.post("/reset")
    assert response.status_code == 200
    assert response.text == "OK"

def test_get_balance_non_existing_account():
    client.post("/reset")
    response = client.get("/balance?account_id=1234")
    assert response.status_code == 404
    assert response.text == "0"

def test_create_account_with_initial_balance():
    client.post("/reset")
    response = client.post("/event", json={"type": "deposit", "destination": "100", "amount": 10})
    assert response.status_code == 201
    assert response.json() == {"destination": {"id": "100", "balance": 10}}

def test_deposit_to_existing_account():
    client.post("/reset")
    client.post("/event", json={"type": "deposit", "destination": "100", "amount": 10})
    response = client.post("/event", json={"type": "deposit", "destination": "100", "amount": 10})
    assert response.status_code == 201
    assert response.json() == {"destination": {"id": "100", "balance": 20}}

def test_get_balance_existing_account():
    client.post("/reset")
    client.post("/event", json={"type": "deposit", "destination": "100", "amount": 20})
    response = client.get("/balance?account_id=100")
    assert response.status_code == 200
    assert response.text == "20"

def test_withdraw_from_non_existing_account():
    client.post("/reset")
    response = client.post("/event", json={"type": "withdraw", "origin": "200", "amount": 10})
    assert response.status_code == 404
    assert response.text == "0"

def test_withdraw_from_existing_account():
    client.post("/reset")
    client.post("/event", json={"type": "deposit", "destination": "100", "amount": 20})
    response = client.post("/event", json={"type": "withdraw", "origin": "100", "amount": 5})
    assert response.status_code == 201
    assert response.json() == {"origin": {"id": "100", "balance": 15}}

def test_transfer_from_existing_account():
    client.post("/reset")
    client.post("/event", json={"type": "deposit", "destination": "100", "amount": 15})
    response = client.post("/event", json={"type": "transfer", "origin": "100", "amount": 15, "destination": "300"})
    assert response.status_code == 201
    assert response.json() == {
        "origin": {"id": "100", "balance": 0},
        "destination": {"id": "300", "balance": 15}
    }

def test_transfer_from_non_existing_account():
    client.post("/reset")
    response = client.post("/event", json={"type": "transfer", "origin": "200", "amount": 15, "destination": "300"})
    assert response.status_code == 404
    assert response.text == "0"