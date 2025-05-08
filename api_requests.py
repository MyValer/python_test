from api_settings import API_BASE_URL, CREATE_DELIVERY_PATH, TRACK_DELIVERY_PATH
import requests

def post_new_delivery(order_info):
    """Отправляет запрос на создание новой доставки"""
    return requests.post(API_BASE_URL + CREATE_DELIVERY_PATH,
                       json=order_info)

def check_delivery_status(tracking_code):
    """Проверяет статус доставки по трек-номеру"""
    return requests.get(f"{API_BASE_URL}{TRACK_DELIVERY_PATH}?t={tracking_code}")