from api_requests import post_new_delivery, check_delivery_status  # Исправленный импорт
from order_data import sample_order  # Используем новое имя для тестовых данных


def test_get_order_info_by_track():
    # 1. Создаем заказ
    response = post_new_delivery(sample_order)  # Используем новое имя функции

    # 2. Получаем трек-номер
    track_number = response.json()['track']

    # 3. Запрашиваем данные по треку
    order_info = check_delivery_status(track_number)  # Используем новое имя функции

    # 4. Проверяем статус код
    assert order_info.status_code == 200, f"Ожидался код 200, получен {order_info.status_code}"

    # 5. Дополнительная проверка данных
    assert 'order' in order_info.json(), "В ответе отсутствует информация о заказе"