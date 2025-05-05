import requests
import logging
import os


class OrderAPI:
    BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1"

    def __init__(self):
        # Настройка логирования
        log_dir = "/var/www/backend/logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)

        logging.basicConfig(
            filename=os.path.join(log_dir, "error.log"),
            level=logging.ERROR,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    def create_order(self, order_data):
        """Создание заказа"""
        url = f"{self.BASE_URL}/orders"
        try:
            response = requests.post(url, json=order_data)
            response.raise_for_status()
            return response
        except Exception as e:
            logging.error(f"Ошибка при создании заказа: {str(e)}")
            raise

    def get_order_by_track(self, track_number):
        """Получение заказа по трек-номеру"""
        url = f"{self.BASE_URL}/orders/track"
        try:
            params = {"t": track_number}
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response
        except Exception as e:
            logging.error(f"Ошибка при получении заказа по треку {track_number}: {str(e)}")
            raise