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
# числа которые БОЛЬШЕ 9 и меньше 100

# -------------------------------------------------------------------

a = [14, 0, 5, 79, 645, 7952, 18, 0, 192, 471]
b = [i for i in a if i % 10 == 2]
print(b)
# [7952, 192]
