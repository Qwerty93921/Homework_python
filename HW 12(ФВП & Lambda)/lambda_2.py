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
# VN: пустой return легко сделать в лямбде: lambda: None

