# Быстрая сортировка

user_in = input("Введите числа через запятую: ")
user_in = user_in.split(',')
my_list = list(map(lambda x: int(x), user_in))

def quick_sort(the_list, key = None):
    if key == None:
        if len(the_list) <= 1:
            return the_list
        pivot = the_list[0]
        less = list(filter(lambda x:  x < pivot, the_list))
        # less = [x for x in the_list if x < pivot]
        equals = list(filter(lambda x: x == pivot, the_list))
        more = list(filter(lambda x: x > pivot, the_list))
        result = quick_sort(less) + equals + quick_sort(more)
        return result
    else:
        return sorted(my_list, key = key)


print(quick_sort(my_list), "Вывод по возрастанию")
print(quick_sort(my_list, key=lambda x: x * -1), "Вывод чисел при умножении на -1")
# 4,1,-123,512,-6,-2,1024

# [-123, -6, -2, 1, 4, 512, 1024] Вывод по возрастанию
# [1024, 512, 4, 1, -2, -6, -123] Вывод чисел при умножении на -1
