def compare(a,b):
    if a > b:
        print("1")
    elif a < b:
        print("-1")
    elif a == b:
        print("0")
        # VN: по условию, функция должна возвращать значения, а не печатать их


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

compare(a, b)

# Это примеры для себя несвязанные с ДЗ---------------------------------------

# def square(x):
#     print("Квадрат числа ", x, "=", x**2)

# square(7)
# 49


# def sayHello():
#     print("Hello")
#     print("World")
#     print("!!!")

# sayHello()

# RETURN = Выход из функции(как break в цикле)
# Если return много, то выполнится самый ПЕРВЫЙ