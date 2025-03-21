user_password = "qwerty123456"

while True:
    user_input = input("Введите пароль: ")
    if user_input == user_password:
        print("Верный пароль.")
        break
    else:
        print("Неверный пароль.")