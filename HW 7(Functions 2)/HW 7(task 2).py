def get_day_of_the_week(day = 1):
    if day == 1:
        name_of_day = "Понедельник"
    elif day == 2:
        name_of_day = "Вторник"
    elif day == 3:
        name_of_day = "Среда"
    elif day == 4:
        name_of_day = "Четверг"
    elif day == 5:
        name_of_day = "Пятница"
    elif day == 6:
        name_of_day = "Суббота"
    elif day == 7:
        name_of_day = "Воскресенье"
    print("День недели - ", name_of_day)

    answer_of_user = input("Желаете заглянуть в будущее? \n")
    if answer_of_user == "Да" or "да" or "Yes" or "yes":
        day = day + 1
        if day > 7:
            day = 1
        get_day_of_the_week(day)

get_day_of_the_week()
