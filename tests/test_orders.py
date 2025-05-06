from helpers.api import ScooterAPI
#  Макаров Валерий, 29-я когорта — Финальный проект. Инженер по тестированию плюс
def test_order_creation():
    api = ScooterAPI()
    order_data = {
        "firstName": "Тест",
        "lastName": "Тестов",
        "address": "Москва",
        "metroStation": 1,
        "phone": "+79999999999",
        "rentTime": 1,
        "deliveryDate": "2024-01-01",
        "comment": "Тест",
        "color": ["BLACK"]
    }
    response = api.create_order(order_data)
    assert response.status_code == 201