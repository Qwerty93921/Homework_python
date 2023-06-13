try:

    text = str(input("Введите слово из 3-х букв: "))

    first_letter = text[0]
    second_letter = text[1]
    third_letter = text[2]

    first_code = ord(first_letter)
    second_code = ord(second_letter)
    third_code = ord(third_letter)

    sum_of_codes = first_code + second_code + third_code

    message_1 = "Коды символов: %d, %d, %d" % (first_code, second_code, third_code)
    message_2 = "Сумма кодов символов = %d" % sum_of_codes


finally:
    print(message_1)
    print(message_2)

#Здесь не может быть ошибок, числа принимаются