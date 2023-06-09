from functools import reduce

# MAP ----------------------------------------------------------

# class map(object):
#     map(func, iterables) _--> map object


def function(x):
    return x ** 2

a = [-1, 2, -3, 4, 5]
b = list(map(function, a))

print(b)

# [1, 4, 9, 16, 25]
# Все числа из списка прошли через функцию степень квадрат
# -------------------------------------------------------------------

a = ["Hello", "hi", "good morning"]
b = list(map(len, a))

print(b)
# [5, 2, 12]
# -------------------------------------------------------------------

a = ["Hello", "hi", "good morning"]
b = list(map(str.upper, a))

print(b)
# ['HELLO', 'HI', 'GOOD MORNING']
# -------------------------------------------------------------------

a = ["Hello", "hi", "good morning"]
b = list(map(lambda x: x[::-1], a))
c = [i[::-1] for i in a]

print(b)
print(c)
# b = ['olleH', 'ih', 'gninrom doog'] - ОБРАТНЫЙ порядок букв
# c = ['olleH', 'ih', 'gninrom doog']
# -------------------------------------------------------------------

a = ["hello", "hi", "good morning"]
b = list(map(list, a))
c = list(map(sorted, b))

print(c)
# [['e', 'h', 'l', 'l', 'o'], ['h', 'i'], [' ', 'd', 'g', 'g', 'i', 'm', 'n', 'n', 'o', 'o', 'o', 'r']]
# В АЛФАВИТНОМ ПОРЯДКЕ встали буквы
# -------------------------------------------------------------------

s = list(map(int, input().split()))

print(s)

# надо ввести цифры через ПРОБЕЛ 
# 4 56 32 542 4545 12 1 ------ ВВОД
# [4, 56, 32, 542, 4545, 12, 1] - РЕЗУЛЬТАТ


# -------------------------------------------------------------------

# Filter ----------------------------------------------------------------

# class filter(object)
#     filter(function or None, iterable) ---> filter object

# def function(x):
#     if x > 10:
#         return True
#     else:
#         return False

# -------------------------------------------------------------------

def function(x):
    return x > 9 and x < 100

# 2 Функции РАВНЫ по смыслу

a = [14, 0, 5, 79, 645, 7952, 18, 0, 192, 471]
b = list(filter(function, a))

print(b)
# [14, 79, 18]
# числа которые БОЛЬШЕ 0

# -------------------------------------------------------------------

a = [14, 0, 5, 79, 645, 7952, 18, 0, 192, 471]
b = [i for i in a if i % 10 == 2]
print(b)
# [7952, 192]

# ---------------------------------------------------------------------------------

# Lambda ---------------------------------------------------------------------------

# def f(x):
#     return x ** 2

# lambda argument_1,argument_2 and etc: действия в функции


r = lambda x: x ** 2

print(r(7))
# 49

# ---------------------------------------------------------------------------------------

# def perimetr(a, b, c):
#     return a + b + c


# print(perimetr(1, 2, 3))



per = lambda a, b, c: a + b + c
print(per(1, 2, 3))
# 6


word = lambda: "Hello"
print(word())
# Hello

# Лямбда не работает с функциями с ЦИКЛАМИ или которые ничего не возвращают(пустой return)

# ------------------------------------------------------------------------------------

def linear(k, b):
    return lambda x: x * k + b

graf_1 = linear(2, 5)
print(graf_1(3))

# 3 * 2 + 5 = 6 + 5 = 11


graf_2 = linear(-4, 1)
print(graf_2(5))

# 5 * (-4) + 1 = -20 + 1 = -19

# ---------------------------------------------------------------------------------------

# REDUCE --------------------------------------------------------------------------------


# Функция reduce применяет функцию двух аргументов кумулятивно к элементам итерируемого, необязательно начиная с начального аргумента. Имеет следующий синтаксис:

# reduce(func, iterable[, initial])

# Где func это функция, к которой кумулятивно применяется каждый элемент iterable, а initial необязательное значение, которое помещается перед элементами итерируемого в вычислении и служит значением по умолчанию, когда итерируемый объект пуст. О reduce()должно быть отмечено следующее:

# func требуется два аргумента, первый из которых является первым элементом в iterable (если initial не указан) а второй - вторым элементом в iterable. Если initial указано, то оно становится первым аргументом функции func, а первый элемент в iterable становится вторым элементом.
# Функция reduce "уменьшает" iterable до одного значения.

# Давайте создадим нашу собственную версию встроенной функции sum(). Функция sum() возвращает сумму всех элементов итерируемого объекта, переданных ей.

numbers = [3, 4, 6, 9, 34, 12]

def custom_sum(first, second):
    return first + second

result = reduce(custom_sum, numbers)
print(result)

# from functools import reduce - в начале сверху надо ввести
# 68

# Как обычно, все дело в итерациях: reduce берет первый и второй элементы в numbers и передает их соответственно в custom_sum. custom_sum вычисляет 
# их сумму и возвращает ее в reduce. Затем reduceпринимает этот результат и применяет его в качестве первого элемента к custom_sum и принимает следующий элемент (третий) 
# в numbers в качестве второго элемента для custom_sum. Он делает это непрерывно (накопительно), пока numbers не будет исчерпан.
