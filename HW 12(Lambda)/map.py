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
