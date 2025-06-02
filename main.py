from fastapi import FastAPI, HTTPException
from models import Event
from service import AccountService

app = FastAPI()
service = AccountService()

@app.post("/reset")
def reset():
    service.reset()
    return {}

@app.get("/balance")
def get_balance(account_id: str):
    balance = service.get_balance(account_id)
    if balance is None:
        raise HTTPException(status_code=404, detail=0)
    return balance

@app.post("/event")
def handle_event(event: Event):
    result = service.handle_event(event)
    if result is None:
        raise HTTPException(status_code=404, detail=0)
    return result
