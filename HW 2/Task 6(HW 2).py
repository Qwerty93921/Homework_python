user_input1 = int(input("Введите первое число: "))
user_input2 = int(input("Введите второе число: "))

a = user_input1
b = user_input2

# formula = a * x + b == 0

if a == 0 and b != 0:
    print("Число не может быть подобрано")
elif a == 0 and b == 0:
    print("x равен любому числу")
else:
    if b == 0 and a != 0:
        pass
    else:
        x = -b / a
        print("X =", x)
