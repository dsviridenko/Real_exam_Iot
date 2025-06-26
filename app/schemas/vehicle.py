from pydantic import BaseModel
from typing import Optional


# Модель данных
class Vehicle(BaseModel):
    id: int
    mark: str
    model: str
    state_number: str
    year_of_realise: str
    status: str


class VehicleCreate(BaseModel):
    mark: str
    model: str
    state_number: str
    year_of_realise: str
    status: str