from api_client import ScooterApi
from order_data import TEST_ORDER_DATA
import json


def print_step(step_num, description):
    print(f"\n[Шаг {step_num}] {description}")


def test_order_workflow():
    print("\n" + "=" * 50)
    print("НАЧАЛО ТЕСТА: Проверка workflow создания заказа")
    print("=" * 50)

    # 1. Создание заказа
    print_step(1, "Создание нового заказа")
    print(f"Отправляемые данные:\n{json.dumps(TEST_ORDER_DATA, indent=2, ensure_ascii=False)}")

    response = ScooterApi.create_order(TEST_ORDER_DATA)
    print(f"Статус ответа: {response.status_code}")
    assert response.status_code == 201, "Ошибка: заказ не создан"
    print("✓ Заказ успешно создан")

    # 2. Получение трек-номера
    print_step(2, "Получение трек-номера")
    track = response.json()["track"]
    print(f"Трек-номер: {track}")
    assert track, "Ошибка: трек-номер не получен"

    # 3. Проверка заказа по треку
    print_step(3, "Проверка заказа по трек-номеру")
    order_info = ScooterApi.get_order_by_track(track)
    print(f"Статус ответа: {order_info.status_code}")
    assert order_info.status_code == 200, "Ошибка: не удалось получить данные заказа"

    # 4. Проверка данных заказа
    print_step(4, "Проверка данных заказа")
    order_data = order_info.json()
    print("Полученные данные заказа:")
    print(json.dumps(order_data, indent=2, ensure_ascii=False))
    assert order_data.get("order"), "Ошибка: данные заказа отсутствуют"

    print("\n" + "=" * 50)
    print("ТЕСТ УСПЕШНО ЗАВЕРШЕН!")
    print("=" * 50)