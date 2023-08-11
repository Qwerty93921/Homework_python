# Задача: Отсортировать словарь по значению в порядке
# возрастания.

fruits = {"apple": 5, "banana": 2, "cherry": 7, "orange": 3} # Создание словаря

# Сортировка словаря по значению
result = {k: v for k, v in sorted(fruits.items(), # sorted - по возрастанию 
key=lambda item: item[1])} # lambda - функция в 1 строку
 
print(result) # Вывод результата

# {'banana': 2, 'orange': 3, 'apple': 5, 'cherry': 7}
