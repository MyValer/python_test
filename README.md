# Автоматизированное тестирование API для сервиса заказов самокатов

Этот проект содержит автоматизированные тесты для API сервиса аренды самокатов.

## 📌 Требования

- Python 3.8+
- Установленные зависимости из `requirements.txt`

## 🛠 Установка

1. Клонируйте репозиторий:
   bash
   git clone https://github.com/MyValer/python_test.git

2.Перейдите в директорию проекта:
  cd python_test

3.Создайте и активируйте виртуальное окружение:
 python -m venv .venv
 # Для Windows:
 .venv\Scripts\activate
 # Для MacOS/Linux:
 source .venv/bin/activate

4.Установите зависимости:
  pip install -r requirements.txt

🚀 Запуск тестов
Основная команда для запуска тестов:
pytest tests/ -v
