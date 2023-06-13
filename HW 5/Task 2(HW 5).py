try:
    user_input = int(input("Введите 3-х значное число: "))

except ValueError:
    print("Вы ввели не число")

else:
    # number_1 = user_input / 100
    # number_2 = (user_input / 10) % 10
    # number_3 = (user_input % 10)

    number_1 = user_input / 100
    number_2 = (user_input / 1000) % 10
    number_3 = (user_input / 100) % 10

    if(number_1 == number_2 or number_2 == number_3 or number_1 == number_3):
        print("Цифры совпали")
    else:
        print("Совпадений нет")
