user_input1 = int(input("Сколько сейчас часов? "))
hours = int(user_input1)

user_input2 = int(input("Сколько сейчас минут? "))
minutes = int(user_input2)

hours_remain = 23 - hours
minutes_remain = 60 - minutes

print("Осталось", hours_remain, "часов", minutes_remain, "минут")
