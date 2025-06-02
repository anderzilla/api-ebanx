from fastapi import FastAPI, Response
from fastapi.responses import Response
from service import service_instance as service
from routes.event import router as event_router

app = FastAPI()

@app.post("/reset")
def reset() -> Response:
    """
    Reseta o estado da aplicação (zera todas as contas).
    Retorna: 200 OK com corpo vazio (text/plain)
    """
    service.reset()
    return Response(status_code=200, content="OK", media_type="text/plain")

@app.get("/balance")
def get_balance(account_id: str) -> Response:
    """
    Retorna o saldo da conta informada.
    Se a conta não existir, retorna 404 com corpo "0" em text/plain.
    """
    balance = service.get_balance(account_id)
    if balance is None:
        return Response(content="0", status_code=404, media_type="text/plain")
    return Response(content=str(balance), status_code=200, media_type="text/plain")

# Inclui o endpoint POST /event de forma modular
app.include_router(event_router)
