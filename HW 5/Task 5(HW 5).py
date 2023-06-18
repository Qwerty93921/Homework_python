user_input1 = int(input("Введите количество $ у вас: "))
dollar = user_input1

user_input2 = int(input("В какую валюту вы хотите перевести доллары? EUR, UAN, AZN(Выберите с помощью клавиш 1, 2, 3) "))
choice = user_input2

eur = dollar * 0.91
uan = dollar * 7.12
azn = dollar * 1.7

if choice == 1:
    choice = eur
    print("Вы выбрали евро")
elif choice == 2:
    choice = uan
    print("Вы выбрали юань")
elif choice == 3:
    choice = azn
    print("Вы выбрали azn")



if choice == eur:
    print("У вас столько евро: ", eur)
elif choice == uan:
    print("У вас столько юаней: ", uan)
elif choice == azn:
    print("У вас столько azn: ", azn)
else:
    print("Такой валюты нет")
