user_input_1 = int(input("Введите первое число от скольки: "))
start_ = user_input_1

user_input_2 = int(input("Введите второе число до скольки: "))
end_ = user_input_2

sum_ = 0

for i in range(start_, end_ + 1):
    sum_ = sum_ + i

print("Сумма чисел в диапозоне =", sum_)
