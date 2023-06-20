try:
    user_input = int(input("Введите 3-х значное число: "))

except ValueError:
    print("Вы ввели не число")

else:
    # number_1 = user_input / 100
    # number_2 = (user_input / 10) % 10
    # number_3 = (user_input % 10)
                                         # VN: допустим, user_input = 456
    number_1 = user_input / 100          # здесь 4.56
    number_2 = (user_input / 1000) % 10  # здесь 0.456
    number_3 = (user_input / 100) % 10   # здесь 4.56
                                         # и программа думает, что 1я цифра == 3я цифра
                                         # хотя это не так

    if(number_1 == number_2 or number_2 == number_3 or number_1 == number_3):
        print("Цифры совпали")
    else:
        print("Совпадений нет")
