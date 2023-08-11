# Задача: У вас есть список заказов с информацией о продуктах
# и количестве

# Создание словаря в списке
orders = [
    {"product": "apple", "quantity" : 500},
    {"product": "banana", "quantity" : 300},
    {"product": "apple", "quantity" : 200},
    {"product": "orange", "quantity" : 400},
    {"product": "banana", "quantity" : 1000},
]

product_quantity = {}
# Создание словаря для хранения суммарного количества продуктов

for order in orders: # Создание цикла для списка, order - каждый элемент списка
    product = order['product'] # Добавление переменной product и присвоение ей "product" из каждого элемента списка
    quantity = order['quantity'] # Добавление переменной quantity и присвоение ей "quantity" из каждого элемента списка

    if product in product_quantity: # Если есть product в словаре product_quantity
        product_quantity[product] += quantity # Тогда в этот словарь добавить quantity
    else: # Иначе
        product_quantity[product] = quantity # Элемент из product_quantity равно quantity

# Вывод результатов
for product, quantity in product_quantity.items(): # Создание цикла
    print(f'{product}: {quantity}') # Выводить продукт и количество через f строку

# apple: 700
# banana: 1300
# orange: 400
