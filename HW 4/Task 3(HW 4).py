try:
    word = str(input("Введите слово: "))

finally:
    result = word[0] + word[1] + "-" + word[-2] + word[-1]

    print(result)

#Здесь не может быть ошибок, числа принимаются