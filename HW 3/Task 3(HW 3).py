word = str(input("Введите слово: "))

result = word[0] + word[1] + "-" + word[-2] + word[-1]
# VN: можно делать срезы строки: word[0:2] + "-" + word[-2:-1]
# или даже так: word[:2] + "-" + word[-2:]

print(result)
