word = input("Введите слово: ")

a = word[::-1]
if word == a:
    print("Палиндром")
else:
    print("Не палиндром")
