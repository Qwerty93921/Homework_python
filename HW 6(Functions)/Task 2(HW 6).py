def get_sum(num):
    if num == 1:
        return 1
    return num + get_sum(num-1)

num = int(input("Введите целое число: "))

result = get_sum(num)
print("Сумма чисел до вашего числа =", result)
