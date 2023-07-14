# my_list = [20,65,43,69,75,2,7,99,9999]
my_list = [20,65,443,69,75,2,7,99,0]

min_number = min(my_list)
max_number = max(my_list)

min_index = my_list.index(min_number)
max_index = my_list.index(max_number)

result = abs(max_index - min_index) # abs - модуль числа
print("Расстояние между минимальным и максимальным числом составляет:",result)


# VN: ваша программа корректно работает с вашим набором данных.
# для другого набора данных, например [20,65,443,69,75,2,7,99,0] расстояние становится отрицательным!
