import sqlite3
import requests
from bs4 import BeautifulSoup


def create_db():
    conn = sqlite3.connect("search_results.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT,
        frequency INTEGER
    )
    """)
    conn.commit()
    conn.close()


def add_site(url):
    conn = sqlite3.connect("search_results.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM results WHERE url = ?", (url,))
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO results (url, frequency) VALUES (?, ?)", (url, 0))
        conn.commit()
    conn.close()


def update_frequency(url):
    conn = sqlite3.connect("search_results.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE results SET frequency = frequency + 1 WHERE url = ?", (url,))
    conn.commit()
    conn.close()


def get_results():
    conn = sqlite3.connect("search_results.db")
    cursor = conn.cursor()
    cursor.execute("SELECT url, frequency FROM results ORDER BY frequency DESC")
    results = cursor.fetchall()
    conn.close()
    return results


def clear_db():
    conn = sqlite3.connect("search_results.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM results")
    conn.commit()
    conn.close()


def parse_site(url, query):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        text = soup.get_text().lower()
        frequency = text.count(query.lower())
        if frequency > 0:
            update_frequency(url)
        return frequency
    except requests.exceptions.RequestException:
        return 0


def main():
    create_db()

    while True:
        print("\nМеню:")
        print("1. Добавить сайт")
        print("2. Просмотреть результаты поиска")
        print("3. Очистить базу данных")
        print("4. Завершить программу")

        choice = input("Выберите опцию: ")

        if choice == "1":
            url = input("Введите URL сайта: ")
            add_site(url)
            print(f"Сайт {url} добавлен в базу данных.")

            query = input("Введите запрос для поиска на сайте: ")
            frequency = parse_site(url, query)
            if frequency > 0:
                print(f"Запрос '{query}' найден {frequency} раз на сайте {url}.")
            else:
                print(f"Запрос '{query}' не найден на сайте {url}.")

        elif choice == "2":
            results = get_results()
            if results:
                print("Результаты поиска (сортировка по частоте):")
                for url, freq in results:
                    print(f"URL: {url}, Частота: {freq}")
            else:
                print("Нет результатов.")

        elif choice == "3":
            clear_db()
            print("База данных очищена.")

        elif choice == "4":
            break
        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()
