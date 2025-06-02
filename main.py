from fastapi import FastAPI, HTTPException, Response
from models import Event
from service import AccountService
from fastapi.responses import JSONResponse

app = FastAPI()
service = AccountService()

@app.post("/reset")
def reset():
    service.reset()
    return Response(status_code=200)

@app.get("/balance")
def get_balance(account_id: str):
    balance = service.get_balance(account_id)
    if balance is None:
        return Response(content="0", status_code=404, media_type="text/plain")
    return Response(content=str(balance), status_code=200, media_type="text/plain")

@app.post("/event")
def handle_event(event: Event):
    result, status_code = service.handle_event(event)
    if result is None:
        return Response(content="0", status_code=404, media_type="text/plain")
    return JSONResponse(content=result, status_code=status_code)
