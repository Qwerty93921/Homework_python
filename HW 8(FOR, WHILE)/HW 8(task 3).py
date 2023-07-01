user_number = int(input("Введите число: "))

for i in range(1, user_number + 1):
    if user_number / 2 >= 50:
        user_number = user_number / 2
        print(i, user_number)
    else:
        print("Число 50 или меньше достигнуто")
        break
