# Сортировка "пузырьком"

user_in = input("Введите числа через запятую: ")
user_in = user_in.split(',')
my_list = list(map(lambda x: int(x), user_in))
# sorted_input = sorted(my_list, key=abs)
# print(sorted_input, "Вывод значений по модулю")

def bubble_sort(my_list, key = None):
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
        return sorted(my_list, key = key)

print(bubble_sort(my_list), "Вывод по возрастанию")
print(bubble_sort(my_list, key=abs), "Вывод по модулю")

# 4,1,-123,512,-6,-2,1024

# [-123, -6, -2, 1, 4, 512, 1024] Вывод по возрастанию
# [1, -2, 4, -6, -123, 512, 1024] Вывод по модулю
