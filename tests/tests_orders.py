import pytest
from helpers.api import ScooterAPI


@pytest.fixture
def api_client():
    return ScooterAPI()


def test_order_creation_and_retrieval(api_client):
    """Тест создания заказа и получения его по трек-номеру"""
    # 1. Подготовка тестовых данных
    test_order = {
        "firstName": "Валерий",
        "lastName": "Петров",
        "address": "Москва, ул. Тестовая, 123",
        "metroStation": 204,
        "phone": "+79991112233",
        "rentTime": 2,
        "deliveryDate": "2024-06-30",
        "comment": "Тестовый заказ",
        "color": ["BLACK"]
    }

    # 2. Создание заказа
    create_response = api_client.create_order(test_order)
    assert create_response.status_code == 201, "Ошибка создания заказа"

    # 3. Получение трек-номера
    track_number = create_response.json().get("track")
    assert track_number is not None, "Трек-номер не получен"

    # 4. Получение заказа по треку
    get_response = api_client.get_order_by_track(track_number)
    assert get_response.status_code == 200, "Ошибка получения заказа"

    # 5. Проверка данных заказа
    order_data = get_response.json()
    assert order_data.get("order") is not None, "Данные заказа не получены"
    assert order_data["order"]["track"] == track_number, "Несоответствие трек-номеров"