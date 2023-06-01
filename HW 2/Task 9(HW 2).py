user_input = int(input("Введите пятизначное число: "))
number_1 = user_input


template = """
digit_5:  %.0f
digit_4:  %.0f
digit_3:  %.0f
digit_2:  %.0f
digit_1:  %.0f
"""
digit_5 = (number_1 / 1) % 10

digit_4 = (number_1 / 10) % 10
digit_3 = (number_1 / 100) % 10
digit_2 = (number_1 / 1000) % 10
digit_1 = (number_1 / 10000) % 10


print("Число с первой цифрой с конца в начале: ", digit_5,digit_2,digit_3,digit_4)
