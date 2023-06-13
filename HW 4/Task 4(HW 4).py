try:
    text = str(input("Введите слово: "))

    result = len(text) // 2

finally:
    print("Половина слова: ", text[:result])

#Не может быть ошибок, числа принимаются