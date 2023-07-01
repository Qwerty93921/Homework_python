user_list = input("Введите 10 чисел через запятую: ")
modified_list = user_list.split(",")

positive = 0
negative = 0
even = 0 # четные
odd = 0 # нечетные
zeros = 0

for i in modified_list:
    i = int(i.strip()) # Убирает символы в начале и конце строки(пробелы и запятые в этом случае)

    if i > 0:
        positive = positive + 1
    elif i < 0:
        negative = negative + 1
    else:
        zeros = zeros + 1
    if i % 2 == 0:
        even = even + 1
    elif i % 2 != 0:
        odd = odd + 1
        
print("Положительных чисел: ", positive)
print("Отрицательных чисел: ", negative)
print("Нулей:", zeros)
print("Четных чисел: ", even)
print("Нечетных чисел: ", odd)
