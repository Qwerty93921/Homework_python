# Пример методов copy и clear

fruits = {"apple":1, "banana":2, "orange":3}

new_fruits = fruits.copy()
# Создаем копию словаря

new_fruits.clear()
# Очищаем словарь

print(new_fruits) # {}
print(fruits)

# {"apple":1, "banana":2, "orange":3}