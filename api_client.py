import requests
from config import BASE_URL, CREATE_ORDER_PATH, GET_ORDER_PATH

class ScooterApi:
    @staticmethod
    def create_order(order_data):
        url = f"{BASE_URL}{CREATE_ORDER_PATH}"
        return requests.post(url, json=order_data)

    @staticmethod
    def get_order_by_track(track_id):
        url = f"{BASE_URL}{GET_ORDER_PATH}"
        return requests.get(url, params={'t': track_id})