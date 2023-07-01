user_number = str(input("Введите число: "))

move_numbers = int(input("Введите число насколько сдвинуть цифры: "))

changed_number = user_number[move_numbers:] + user_number[:move_numbers]
print(changed_number)
