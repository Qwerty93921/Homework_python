def total_time(seconds):
    hours_from_seconds = seconds // 3600
    minutes_from_seconds = (seconds % 3600) // 60
    seconds_from_seconds = (seconds % 3600) % 60
    time = "{:02d}:{:02d}:{:02d}".format(hours_from_seconds, minutes_from_seconds, seconds_from_seconds)
    # VN: этот способ сильно лучше, чем в задаче 6
    return time

user_input_1 = int(input("Введите секунды: "))
seconds = user_input_1

result = total_time(seconds)
print("Время:",result)
