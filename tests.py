import pytest
from fastapi.testclient import TestClient
from main import app
from app.api.v1.web import vehicle_db
from app.schemas.vehicle import Vehicle

client = TestClient(app)


def test_read_root_pass():
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome" in response.json()["message"]


def test_read_root_fail():
    response = client.get("/invalid")
    assert response.status_code == 404


def test_read_items_pass():
    response = client.get("/vehicles")
    assert response.status_code == 200
    assert len(response.json()) == 5


def test_read_items_fail():
    response = client.get("/vehicles")
    assert not len(response.json()) == 10


def test_read_available_items_pass():
    response = client.get("/vehicles/available")
    assert response.status_code == 200
    assert len(response.json()) == 2

def test_read_available_items_fail():
    response = client.get("/vehicles/available")
    assert not len(response.json()) == 10

def test_read_item_pass():
    response = client.get("/vehicles/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_read_item_fail():
    response = client.get("/vehicles/999")
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]


def test_create_item_pass():
    data = {"mark": "NewCar",
            "model":"Model 1",
            "state_number": "Т999ЕА777",
            "year_of_realise": "2023",
            "status": "active"}
    response = client.post("/vehicles", json=data)
    assert response.status_code == 201
    assert response.json()["mark"] == "NewCar"
    assert response.json()["model"] == "Model 1"
    assert response.json()["state_number"] == "Т999ЕА777"
    assert response.json()["year_of_realise"] == "2023"
    assert response.json()["status"] == "active"


def test_create_item_fail():
    data = {"mark": "NewCar",
            "model": "Model 1",
            "state_number": "Т999ЕА777",
            "year_of_realise": "2023"
            }  # Отсутствует обязательное поле 'status'
    response = client.post("/vehicles", json=data)
    assert response.status_code == 422
    assert "status" in response.text  # Проверка наличия ошибки в ответе


def test_delete_vehicle_pass():
    # Создаем временное транспортное средство для удаления
    test_vehicle = Vehicle(
        id=999,
        mark="TestMark",
        model="TestModel",
        state_number="TST001",
        year_of_realise="2023",
        status="active"
    )
    vehicle_db.append(test_vehicle)

    # Удаляем созданное ТС
    response = client.delete(f"/vehicles/{test_vehicle.id}")
    assert response.status_code == 204

    # Проверяем, что ТС действительно удалено
    response = client.get(f"/vehicles/{test_vehicle.id}")
    assert response.status_code == 404


def test_delete_vehicle_fail():
    non_existent_id = 9999
    response = client.delete(f"/vehicles/{non_existent_id}")

    # Проверяем ответ
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()

    # Проверяем, что количество ТС не изменилось
    response = client.get("/vehicles")
    initial_count = len(response.json())
    response_after = client.get("/vehicles")
    after_count = len(response_after.json())
    assert after_count == initial_count
