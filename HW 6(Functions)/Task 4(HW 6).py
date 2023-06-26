def get_square(a, b=None):
    if b == None:
        S = a * a
    else:
        S =  a * b
    return S


user_input_1 = int(input("Введите длину стороны прямоугольника: "))
a = user_input_1

user_input_2 = int(input("Введите ширину стороны прямоугольника: "))
b = user_input_2


S = get_square(a, b)
print("Площадь прямоугольника =" ,S)


S = get_square(a)
print("Площадь квадрата =" ,S) 
