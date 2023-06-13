try:
    user_input = str(input("Введите слово: "))
    word = user_input


finally:
    amount_of_letters = len(word)
    print("Длина строки составляет", amount_of_letters, "символов")

#Здесь не может быть ошибок, числа принимаются