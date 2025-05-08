import pytest
from api_client import ScooterApi
from order_data import TEST_ORDER_DATA


class TestOrderWorkflow:
    def test_order_creation_and_retrieval(self):
        """Автоматизация сценария: создание заказа и проверка по треку"""

        # Шаг 1: Создание заказа
        create_response = ScooterApi.create_order(TEST_ORDER_DATA)
        assert create_response.status_code == 201, (
            f"Ошибка создания заказа. Код: {create_response.status_code}"
        )

        # Шаг 2: Сохранение трек-номера
        track_number = create_response.json().get("track")
        assert track_number, "Трек-номер не получен в ответе"

        # Шаг 3: Получение заказа по треку
        get_response = ScooterApi.get_order_by_track(track_number)

        # Шаг 4: Проверка кода ответа
        assert get_response.status_code == 200, (
            f"Ожидался код 200, получен {get_response.status_code}"
        )

        # Дополнительная проверка данных
        order_info = get_response.json()
        assert "order" in order_info, "В ответе отсутствует информация о заказе"
        assert order_info["order"]["track"] == track_number, "Несоответствие трек-номеров"