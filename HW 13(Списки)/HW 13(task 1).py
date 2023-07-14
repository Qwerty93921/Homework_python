user_input = input("Введите 10 чисел: ")
user_list = user_input.split(",")

even_list = []

try:
    if len(user_list) < 10:   # VN: вычисление len не может вызвать ValueError. Обработчик здесь не нужен
        print("Вы ввели меньше 10 чисел")

except ValueError():
    print("Введите числа через запятую")

else:
    if len(user_list) >= 10:
        for number in range(len(user_list[0:11])):
            if number % 2 == 0:   # VN: number здесь является индексом. Числа пользователя вы не проверяете на чётность
                even_list.append(user_list[number])
                print("Четное число из списка:", user_list[number])
            else:
                continue
        print("Список четных чисел из первых 10 чисел вашего списка: ", even_list)

# 100,99,98,97,96,95,94,93,92,91,90,89,88,87,86,85,84
# Список четных чисел из первых 10 чисел вашего списка:  ['100', '98', '96', '94', '92', '90']
