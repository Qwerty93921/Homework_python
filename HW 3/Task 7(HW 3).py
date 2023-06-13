user_input_1 = int(input("Введите год рождения: "))
year = user_input_1

user_input_2 = int(input("Введите месяц рождения: "))
month = user_input_2

user_input_3 = int(input("Введите число рождения: "))
date = user_input_3

message = "Дата рождения: %d.%d.%d" % (year, month, date)

print(message)
