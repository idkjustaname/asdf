import requests

try:
    response = requests.get('https://fake-json-api.mock.beeceptor.com/users')
    response.raise_for_status()
    print(response.json())

except requests.exceptions.HTTPError as errh:
    print(f"HTTP ошибка: {errh}")
except requests.exceptions.RequestException as err:
    print(f"Ошибка запроса: {err}")
