import pytest
from api_client import ApiClient
from order_data import DEFAULT_ORDER


class TestOrderCreation:
    def test_create_and_get_order(self):
        # Создание заказа
        response = ApiClient.create_order(DEFAULT_ORDER)
        assert response.status_code == 201

        # Получение заказа
        track = response.json()["track"]
        order_response = ApiClient.get_order(track)

        assert order_response.status_code == 200
        assert order_response.json()["order"]["track"] == track