import requests


class ScooterAPI:
    BASE_URL = "https://0834152a-9c57-4c5a-bc9d-43fa46bc7e34.serverhub.praktikum-services.ru/api/v1"

    def create_order(self, order_data):
        return requests.post(f"{self.BASE_URL}/orders", json=order_data)