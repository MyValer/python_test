import requests
from data.data import order_data

BASE_URL = " https://9e0f4a9f-1947-4e70-b9bd-6c7d2db2b41d.serverhub.praktikum-services.ru"
def test_order_creation():
    # 1. Выполнить запрос на создание заказа.
    response_create = requests.post(f"{BASE_URL}", json=order_data)
    assert response_create.status_code == 201
    response_json = response_create.json()
    # 2. Сохранить номер трека заказа.
    order_track = response_json.get("track")
    assert order_track is not None, "Ответ не содержит номер трека заказа"
    # 3. Выполнить запрос на получение заказа по треку заказа.
    response_get = requests.get(f"{BASE_URL}/track?t={order_track}")
    # 4. Проверить, что код ответа равен 200.
    assert response_get.status_code == 200