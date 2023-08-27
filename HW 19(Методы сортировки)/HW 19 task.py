user_in = input("Введите числа через запятую: ")
user_in = user_in.split(',')
my_list = list(map(lambda x: int(x), user_in))

print(my_list, "- список")

def sort_numbers(my_list, key = None):
    if key == None:
        is_sorted = False
        while not is_sorted:
            is_sorted = True
            for i in range(len(my_list)-1):
                if my_list[i] > my_list[i+1]:
                    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
                    is_sorted = False
        return my_list
    else:
        is_sorted = False
        while not is_sorted:
            is_sorted = True
            for i in range(len(my_list) - 1):
                if key(my_list[i]) > key(my_list[i + 1]):
                    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
                    is_sorted = False
        return my_list

print(sort_numbers(my_list), "Обычная сортировка")
print(sort_numbers(my_list, key=abs), "Вывод по модулю")
print(sort_numbers(my_list, key=lambda x: x % 2), "Остатки чисел после деления на 2 по возрастанию")
print(sort_numbers(my_list, key=lambda x: x * -1), "Вывод чисел при умножении на -1")

# 6, 4, -18, 15, -3, 8, -99, -123

# [6, 4, -18, 15, -3, 8, -99, -123] - список
# [-123, -99, -18, -3, 4, 6, 8, 15] Обычная сортировка
# [-3, 4, 6, 8, 15, -18, -99, -123] Вывод по модулю
# [4, 6, 8, -18, -3, 15, -99, -123] Остатки чисел после деления на 2 по возрастанию
# [15, 8, 6, 4, -3, -18, -99, -123] Вывод чисел при умножении на -1
