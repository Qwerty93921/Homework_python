def get_numbers_combination(number_1, number_2, number_3):
    combined_number = int(str(number_1) + str(number_2) + str(number_3))
    return combined_number

user_input_1 = int(input("Введите первое число: "))
number_1 = user_input_1

user_input_2 = int(input("Введите второе число: "))
number_2 = user_input_2

user_input_3 = int(input("Введите третье число: "))
number_3 = user_input_3

result = get_numbers_combination(number_1, number_2, number_3)
print(result)
