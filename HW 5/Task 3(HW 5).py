user_input = int(input("Введите год: "))

special_year = user_input

if special_year % 400 == 0 or special_year % 4 == 0 and special_year % 100 != 0:
    print("Год високосный")
else:
    print("Год не високосный")
