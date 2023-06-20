user_input = int(input("Введите сумму покупки: "))
sum_ = user_input

if sum_ >= 200 and sum_ < 300:
    sum1 = sum_ - (sum_ * 0.03)
    print("Скидка 3%, сумма к оплате:", sum1)
elif sum_ >= 300 and sum_ < 500:
    sum2 = sum_ - (sum_ * 0.05)
    print("Скидка 5%, сумма к оплате:", sum2)
elif sum_ >= 500:
    sum3 = sum_ - (sum_ * 0.07)
    print("Скидка 7%, сумма к оплате:", sum3)
#VN: else скидки нет, сумма к оплате.. - не хватает этого