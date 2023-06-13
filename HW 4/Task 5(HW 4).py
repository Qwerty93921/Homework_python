try:
    user_input = str(input("Введите текст: "))
    text = user_input[1:-1]

    change = "*" + text + "*"

finally:
    print(change)

#Ошибок нет, числа принимаются