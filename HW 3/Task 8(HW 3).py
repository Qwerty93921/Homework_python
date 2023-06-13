user_input_1 = int(input("Введите стоимость покупок: "))
price = user_input_1

user_input_2 = int(input("Введите вашу скидку в %: "))
discount = user_input_2

percent = discount / 100

number_from_percent = percent * price

result = price - number_from_percent

message = "Ваша сумма к оплате со скидкой составляет %.2f" % (result)

print(message)
