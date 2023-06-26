def get_time(hours, minutes=None, seconds=None):
    time = str(str(hours) + ":" + str(minutes) + ":" + str(seconds))

    if minutes == None and seconds == None:
        time = str(str(hours) + "00:00")
        return time
    elif minutes == None:
        time = str(str(hours) + "00:00")
        return time
    elif seconds == None:
        time = str(str(hours) + str(minutes) + ":00")
    return time

user_input_1 = input("Введите часы: ")
hours = user_input_1

user_input_2 = input("Введите минуты: ")
minutes = user_input_2

user_input_3 = input("Введите секунды: ")
seconds = user_input_3

time = get_time(hours, minutes, seconds)
print("Время:", time)
