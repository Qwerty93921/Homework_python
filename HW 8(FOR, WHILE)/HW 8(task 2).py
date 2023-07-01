user_input_1 = int(input("Введите первое число: "))
number_1 = user_input_1

user_input_2 = int(input("Введите второе число: "))
number_2 = user_input_2

small_number = min(number_1, number_2)

NOD = 1 # В НОД число делится изначально на себя или на 1

for i in range(1, small_number + 1):
    if number_1 % i == 0 and number_2 % i == 0:
        NOD = i

print("НОД =", NOD)
