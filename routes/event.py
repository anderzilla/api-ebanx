from fastapi import APIRouter
from fastapi.responses import JSONResponse, Response
from models import Event
from service import service_instance as service

router = APIRouter()

@router.post("/event")
def handle_event(event: Event) -> Response:
    """
    Processa eventos do tipo:
    - deposit: adiciona saldo à conta (cria se não existir)
    - withdraw: retira saldo de uma conta existente
    - transfer: movimenta saldo entre contas

    Retorna:
    - 201 com JSON em caso de sucesso
    - 404 com corpo "0" (text/plain) se a conta de origem não existir
    """
    result, status_code = service.handle_event(event)

    if result is None:
        return Response(content="0", status_code=404, media_type="text/plain")

    return JSONResponse(content=result, status_code=status_code)
