from pydantic import BaseModel
from typing import Optional

class Event(BaseModel):
    """
    Representa um evento de operação financeira na API:
    - deposit: exige 'destination' e 'amount'
    - withdraw: exige 'origin' e 'amount'
    - transfer: exige 'origin', 'destination' e 'amount'
    """
    type: str
    destination: Optional[str] = None
    origin: Optional[str] = None
    amount: int
