names_list = ["Саша", "Андрей", "Егор", "Роман", "Евгений", "Петрович", "Петрович", "Виктор"]

for name in names_list:
    if names_list.count(name) > 1:
        print("Imposter is found, it is:", name,"!!!", "\nCatch him RIGHT NOW!!!!!11111!!!!1111!!!!111!!!!!!\n")
    else:
        print(name, "is not imposter\n continue searhing...\n")
