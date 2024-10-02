import requests
from datetime import datetime, timedelta

# Визначення URL-адреси API НБУ
nbu_api_url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"

# Задайте початкову та кінцеву дати
start_date = datetime.strptime("2024-09-23", "%Y-%m-%d")
end_date = datetime.strptime("2024-09-29", "%Y-%m-%d")

# Перебір дат з інтервалом у один день
current_date = start_date
while current_date <= end_date:
    # Форматування дати у формат 'YYYYMMDD'
    date_str = current_date.strftime("%Y%m%d")

    # Параметри запиту
    params = {'date': date_str, 'json': ''}

    # Відправка запиту до API НБУ
    response = requests.get(nbu_api_url, params=params)

    if response.status_code == 200:
        # Вивід даних у форматі JSON
        data = response.json()
        print(f"Курс валют на {date_str}:")
        for currency in data:
            print(f"{currency['cc']}: {currency['rate']}")
        print("\n")
    else:
        print(f"Не вдалося отримати дані за {date_str}. Статус код: {response.status_code}")

    # Переходимо до наступного дня
    current_date += timedelta(days=1)
