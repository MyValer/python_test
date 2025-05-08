from config import BASE_URL, CREATE_ORDER_PATH, GET_ORDER_PATH
import requests


class ApiClient:
    @staticmethod
    def create_order(order_data):
        return requests.post(BASE_URL + CREATE_ORDER_PATH, json=order_data)

    @staticmethod
    def get_order(track_id):
        return requests.get(BASE_URL + GET_ORDER_PATH, params={'t': track_id})