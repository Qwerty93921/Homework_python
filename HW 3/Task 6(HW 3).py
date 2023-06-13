user_input_1 = str(input("Введите название фильма: "))
movie = user_input_1

user_input_2 = str(input("Введите название кинотеатра: "))
cinema = user_input_2

user_input_3 = int(input("Введите во сколько начинается кино: "))
time = user_input_3


message = "Билет на %s в кинотеатре %s на время %d забронирован" % (movie, cinema, time)

print(message)
