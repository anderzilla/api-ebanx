from pydantic import BaseModel
from typing import Optional

class Event(BaseModel):
    type: str
    destination: Optional[str] = None
    origin: Optional[str] = None
    amount: int
