user_password = "qwerty123456"
flag = True

while flag:
    user_input = input("Введите пароль: ")
    if user_input == user_password:
        print("Верный пароль.")
        flag = False
    else:
        print("Неверный пароль.")