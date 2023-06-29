import random

def get_random_int(min, max):
    result = random.random() * (max - min)
    result = result + min
    return int(result)

def game(my_random, min, max, tries = 7):

    user_input = input("Угадай число от 0 до 100:\nУ вас попыток %d\n" % tries)
    
    if tries > 0:

        try:
            user_num = int(user_input)
        except ValueError:
            print("Только целое число введи")
            game(my_random, min, max)
        else:
            if my_random > user_num and tries <= 7:
                print("Больше :)\n")
                game(my_random, min, max, tries - 1)
                print("Попыток осталось %d" % tries)
            elif my_random < user_num and tries <= 7:
                print("Меньше :)\n")
                game(my_random, min, max, tries - 1)
                print("Попыток осталось %d" % tries)
            elif my_random != user_num and tries == 0:
                print("Вы проиграли! Число было %d" % my_random)
            elif my_random == user_num and tries > 0:
                print("Вы угадали, число = %d! Осталось попыток %d" % (my_random, tries))
                return

    elif tries == 0:
        print("Попытки закончились, вы проиграли, число было %d" % my_random)
        return



def game_refresher(tries = 0):
        
    user_choice = input("Хотите сыграть еще раз?(да/нет)\n")

    if user_choice == "Да" or "да" or "Yes" or "yes":
        num = get_random_int(0, 100)
        game(num, 0, 100)
        game_refresher(user_choice)
    elif user_choice == "Нет" or "нет" or "No" or "no":
        print("Игра окончена!!!!!!!1111!!!!!!!1111")
    else:
        print("Вы ввели что-то другое")
        return


num = get_random_int(0, 100)
game(num, 0, 100)
# VN: Лучше всего сразу запускать game_refresher, а game уже запускать из неё,
# и в ней получать и проверять user_choice, но уже после вызова game
game_refresher()