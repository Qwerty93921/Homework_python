user_input = input("Введите числа через запятую без пробелов: ")
user_list = user_input.split(",")
# user_list = [3, 9, 8, 4, 5, 1]
# ['9', '5']

bigger_number = []

for i in range(len(user_list) - 1): # - 1 потому что последнее число остается без парного второго числа и оно не учитывается
    if user_list[i] < user_list[i + 1] :
        bigger_number.append(user_list[i + 1])

print(bigger_number)
'''
VN: Ваша программа не работает:
Введите числа через запятую без пробелов: 4,3,2,11,0
[]
'''