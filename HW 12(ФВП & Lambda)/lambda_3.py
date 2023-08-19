def linear(k, b):
    return lambda x: x * k + b

graf_1 = linear(2, 5)
print(graf_1(3))

# 3 * 2 + 5 = 6 + 5 = 11


graf_2 = linear(-4, 1)
print(graf_2(5))

# 5 * (-4) + 1 = -20 + 1 = -19

