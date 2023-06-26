def get_seconds(hours, minutes, seconds):
    seconds_from_hours = hours * 3600
    seconds_from_minutes = minutes * 60
    seconds_from_seconds = seconds * 1
    sum_ = seconds_from_hours + seconds_from_minutes + seconds_from_seconds
    return sum_

user_input_1 = int(input("Введите часы: "))
hours = user_input_1

user_input_2 = int(input("Введите минуты: "))
minutes = user_input_2

user_input_3 = int(input("Введите секунды: "))
seconds = user_input_3

result = get_seconds(hours, minutes, seconds)
print("Столько секунд в сумме:",result)
