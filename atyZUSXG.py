import requests
from bs4 import BeautifulSoup

def get_exchange_rate():
    url = "https://www.cbar.az/currency-rates"
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    dollar_row = soup.find('td', text='USD')
    if dollar_row:
        return float(dollar_row.find_next('td').text.strip().replace(',', '.'))
    raise ValueError("Не удалось найти курс доллара.")

def main():
    try:
        exchange_rate = get_exchange_rate()
        amount = float(input("Введите количество манатов: "))
        print(f"Это эквивалентно {amount / exchange_rate:.2f} долларов США.")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
