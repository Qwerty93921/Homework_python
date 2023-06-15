user_input_1 = int(input("Введите год рождения: "))
year = user_input_1

user_input_2 = int(input("Введите месяц рождения: "))
month = user_input_2

user_input_3 = int(input("Введите число рождения: "))
date = user_input_3

message = "Дата рождения: %d.%d.%d" % (year, month, date)

print(message)

'''
Введите год рождения: 2010
Введите месяц рождения: 3
Введите число рождения: 3
Дата рождения: 2010.3.3

Должно быть: 03.03.2010
'''
