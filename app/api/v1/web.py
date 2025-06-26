from fastapi import APIRouter, HTTPException, status
from typing import List
from app.schemas.item import Vehicle, VehicleCreate
from app.db.database import vehicle_db

router = APIRouter()

@router.get("/", summary="Корневая страница")
def read_root():
    return {"message": "Welcome to FastAPI REST Server"}


@router.get("/vehicles", response_model=List[Vehicle], summary="Получить все автотранспортные средства")
def read_items():
    return vehicle_db

@router.get("/vehicles/available", response_model=List[Vehicle], summary="Получить свободные ТС")
def read_items():
    return [item for item in vehicle_db if item.status == 'свободен']

@router.get("/vehicles/{id}", response_model=Vehicle, summary="Получить информацию о ТС")
def read_item(id: int):
    item = next((i for i in vehicle_db if i.id == id), None)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.post("/vehicles", response_model=Vehicle,
          status_code=201,
          summary="Добавить новое ТС")
def create_item(item: VehicleCreate):
    next_id = vehicle_db[::-1][0].id + 1
    new_item = Vehicle(id=next_id,
                       mark=item.mark,
                       model=item.model,
                       state_number=item.state_number,
                       year_of_realise=item.year_of_realise,
                       status=item.status)
    vehicle_db.append(new_item)
    if len(vehicle_db) != next_id:
        raise HTTPException(status_code=404, detail="Item not found")
    return new_item


@router.delete("/vehicles/{id}", status_code=204, summary="Списать ТС")
def delete_item(id: int):
    global vehicle_db
    initial_length = len(vehicle_db)
    vehicle_db = [item for item in vehicle_db if item.id != id]

    if len(vehicle_db) == initial_length:
        raise HTTPException(status_code=404, detail="Item not found")
    return

