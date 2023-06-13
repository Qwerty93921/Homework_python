try:
    user_input = int(input("Введите число от 1 до 9: "))

except ValueError:
    print("Вы ввели не число от 1 до 9")

else:
    if user_input == 1:
        print("!")
    elif user_input == 2:
        print("@")
    elif user_input == 3:
        print("#")
    elif user_input == 4:
        print("$")
    elif user_input == 5:
        print("%")
    elif user_input == 6:
        print("^")
    elif user_input == 7:
        print("&")
    elif user_input == 8:
        print("*")
    elif user_input == 9:
        print("(")
