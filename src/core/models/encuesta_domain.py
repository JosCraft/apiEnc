from pydantic import BaseModel
from typing import Optional
from datetime import date

class EncuestaDomain(BaseModel):
    id: Optional[int] = 0
    fecha: date
