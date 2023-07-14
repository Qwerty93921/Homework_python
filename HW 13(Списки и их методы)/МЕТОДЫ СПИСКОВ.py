first_list = [1, 2, 3, 4, 5]
second_list = [6, 7, 8, 9]

first_list.append(6)
print(first_list)

first_list.extend(second_list)
print(first_list)

first_list.insert(4, "торт")
print(first_list)
###############################

third_list = [1, 2, 5, True, "cake", "ololo"]
element_removed = third_list.remove("cake")
print(third_list, element_removed)

element_popped = third_list.pop(3)
print(third_list, element_popped)

third_list.clear()
print(third_list)
###############################


first_list = [1, 2, 5, True, "cake", "ololo"]
something = "ololo"
my_index = first_list.index(something)
print(my_index)  # 5

###############################

first_list = [1, "cake", 2, 5, False, "cake", "ololo", "cake"]
total = first_list.count("cake")
print(first_list)
print("Total -", total)

###############################

third_list = ["slovo", "nut", "mars", "olovo", "yetti"]
result = third_list.sort(reverse=True)

print(third_list)
print(result)

###############################

forth_list = ["Hello", 666, 0, "sun", [8, 7, 6]]
forth_list.reverse()
print(forth_list)

fifth_list = forth_list.copy()
# fifth_list = forth_list
fifth_list[2] = "welcome"
fifth_list[0][2] = "A"

print(fifth_list)
print(forth_list)

print(fifth_list is forth_list)


# append(item) -- добавление нового элемента в конец списка;
# extend(list) -- добавляет элементы из списка в конец другого
# списка;
# insert(item) -- вставляет элемент по указанному индексу;

# remove(item) -- удаляет элемент из списка;
# pop(index) -- возвращает элемент по указанному индексу и
# удаляет его из списка;
# clear() -- удаляет все элементы из списка;

# index(item) -- возвращает индекс указанного элемента;
# count(item) -- возвращает количество указанных элементов в
# списке;
# sort(key=None, reverse=False) -- сортирует список в порядке
# возрастания или убывания;
# В качестве key можно передать функцию с одним аргументом,
# которая будет использоваться для получения ключа сравнения из
# каждого элемента списка.

# reverse() -- возвращает список в обратном порядке;
# copy() -- возвращает поверхностную копию списка.
# Примечание: Поверхностная копия создает новый составной
# объект, и затем (по мере возможности) вставляет в него ссылки
# на объекты, находящиеся в оригинале. Глубокая копия создает
# новый составной объект, и затем рекурсивно вставляет в него
# копии объектов, находящихся в оригинале.

# Абстракция списков (List Comprehension) — это лаконичный и
# элегантный способ создания списков. Абстракция списков
# состоит из выражения, за которым следует оператор for в
# квадратных скобках.
# Вот пример создания списка, в котором каждый элемент
# возводится в степень 2:

# numbers = [number ** 2 for number in range(1, 6)]

# -----------------------------------------------------------------------------------------------------------

# user_list = [int(num) for num in user_list] ---------------------------------------------------------------------------------------------
# ПРЕОБРАЗОВАЕТ ЭЛЕМЕНТЫ СПИСКА В INT ФОРМАТ ПОСЛЕ SPLIT от USER INPUT
