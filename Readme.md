# Автоматизированное тестирование API сервиса доставки

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Pytest](https://img.shields.io/badge/Pytest-7.0+-green)
![Requests](https://img.shields.io/badge/Requests-2.25+-yellow)

Проект автоматизированного тестирования REST API для сервиса доставки.

## 📝 Содержание

- [Структура проекта](#-структура-проекта)
- [Технологии](#-технологии)
- [Установка](#%EF%B8%8F-установка)
- [Запуск тестов](#-запуск-тестов)
- [Тестовые сценарии](#-тестовые-сценарии)
- [Конфигурация](#%EF%B8%8F-конфигурация)
- [Отчеты](#-отчеты)


## 📂 Структура проекта
delivery_api_tests/
├── api/
│ ├── client.py # Клиент для работы с API
│ └── endpoints.py # Все эндпоинты API
├── data/
│ └── test_data.py # Тестовые данные
├── tests/
│ └── test_orders.py # Тестовые сценарии
├── config.py # Настройки окружения
├── requirements.txt # Зависимости
├── .gitignore # Исключаемые файлы
└── README.md # Документация


## 🛠 Технологии

- Python 3.8+
- Pytest - фреймворк для тестирования
- Requests - отправка HTTP-запросов


## ⚙️ Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/ваш-username/название-репозитория.git
cd delivery_api_tests
Установите зависимости:

bash
pip install -r requirements.txt

🚀 Запуск тестов
Базовый тест:

bash
pytest tests/test_orders.py -v
С подробным выводом:

bash
pytest tests/test_orders.py -v -s
С генерацией отчета Allure:

🧪 Тестовые сценарии
test_create_order - создание нового заказа

Проверка кода ответа (201)

Проверка наличия трек-номера

test_get_order_by_track - получение заказа по треку

Проверка кода ответа (200)

Проверка структуры ответа

Проверка соответствия данных

⚙️ Конфигурация
Основные настройки в config.py:

python
BASE_URL = "https://65a9011b-cf45-414a-85f8-968d719da8b0.serverhub.praktikum-services.ru"
TIMEOUT = 10  # Таймаут запросов в секундах
LOG_LEVEL = "INFO"  # Уровень логирования
📊 Отчеты
Тесты выводят в консоль:

Отправляемые данные

Статус-коды ответов

Время выполнения

Ошибки (если есть)

Для более наглядных отчетов рекомендуется использовать Allure.
