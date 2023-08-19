# Сортировка выборкой

user_in = input("Введите числа через запятую: ")
user_in = user_in.split(',')
my_list = list(map(lambda x: int(x), user_in))


def select_sort(my_list, key = None):
    if key == None:
        sorted_list = []
        for _ in range(len(my_list)):
            # min_elem = min(my_list)
            # sorted_list.append(min_elem)
            # del my_list[my_list.index(min_elem)]
            min_index = 0
            for k in range(1, len(my_list)):
                if my_list[k] < my_list[min_index]:
                    min_index = k
            sorted_list.append(my_list[min_index])
            del my_list[min_index]
        return sorted_list
    else:
        return sorted(my_list, key = key)

# my_list = sorted_list
print(select_sort(my_list.copy()), "Вывод по возрастанию")
print(select_sort(my_list, key=lambda x: x % 2), "Остатки чисел после деления на 2 по возрастанию")

# 4,1,-123,512,-6,-2,1024

# [-123, -6, -2, 1, 4, 512, 1024] Вывод по возрастанию
# [4, 512, -6, -2, 1024, 1, -123] Остатки чисел после деления на 2 по возрастанию
