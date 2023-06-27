def get_sum(num):
    if num == 1:  # VN: для надёжности лучше использовать <=
        return 1  # И возвращать не 1, а num. Вдруг вам дробное число передадут в функцию
    return num + get_sum(num-1)

num = int(input("Введите целое число: "))

result = get_sum(num)
print("Сумма чисел до вашего числа =", result)
