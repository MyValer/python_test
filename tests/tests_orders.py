import pytest
import logging
from helpers.api import OrderAPI


@pytest.fixture
def order_api():
    return OrderAPI()


def test_create_and_get_order(order_api):
    """Тест создания заказа и проверки его данных по трек-номеру"""
    try:
        # Шаг 1: Создание заказа
        order_data = {
            "firstName": "Иван",
            "lastName": "Иванов",
            "address": "Москва, ул. Ленина, 1",
            "metroStation": 4,
            "phone": "+79991112233",
            "rentTime": 3,
            "deliveryDate": "2024-06-30",
            "comment": "Тестовый заказ",
            "color": ["BLACK"]
        }

        create_response = order_api.create_order(order_data)
        assert create_response.status_code == 201, "Не удалось создать заказ"

        # Шаг 2: Сохранение номера трека
        track_number = create_response.json().get("track")
        assert track_number is not None, "Трек-номер не получен в ответе"

        # Шаг 3: Получение заказа по треку
        get_response = order_api.get_order_by_track(track_number)

        # Шаг 4: Проверка кода ответа
        assert get_response.status_code == 200, "Не удалось получить заказ по трек-номеру"

    except Exception as e:
        logging.error(f"Ошибка в тесте: {str(e)}")
        raise