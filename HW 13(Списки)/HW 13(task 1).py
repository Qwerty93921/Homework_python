user_input = input("Введите 10 чисел: ")
user_list = user_input.split(",")
user_list = [int(num) for num in user_list] # Элементы принимают int формат после split
print(user_list)

even_list = []

if len(user_list) < 10:   # VN: вычисление len не может вызвать ValueError. Обработчик здесь не нужен
    print("Вы ввели меньше 10 чисел")


if len(user_list) >= 10:
    for number in range(len(user_list[0:11])):
        if user_list[number] % 2 == 0:   # VN: number здесь является индексом. Числа пользователя вы не проверяете на чётность
            even_list.append(user_list[number])
            print("Четное число из списка:", user_list[number])
        else:
            continue
    print("Список четных чисел из первых 10 чисел вашего списка: ", even_list)

# 100,99,98,97,96,95,94,93,92,91,90,89,88,87,86,85,84
# Список четных чисел из первых 10 чисел вашего списка:  ['100', '98', '96', '94', '92', '90']

# 1,2,3,4,5,6,7,8,9,10,11,12,13,14
