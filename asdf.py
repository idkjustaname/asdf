try:
    user_input = input("Введите строку: ")

    if not user_input.isalpha():
        raise ValueError("Строка должна содержать только буквы.")

    print("Введенная строка: ", user_input)
    print("No errors")

except ValueError as error:
    print(f"Ошибка: {error}")

except Exception as e:
    print(f"Неизвестная ошибка: {e}")

print("Код после блока try-except")
