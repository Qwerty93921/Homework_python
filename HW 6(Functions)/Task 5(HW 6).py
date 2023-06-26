def get_tub_volume(diameter, height):
    r = diameter / 2
    S = 3.14 * (r ** 2)
    volume = S * height * 1000
    return volume

# Умножаем на 1000 для перевода в литры

user_input_1 = int(input("Введите диаметр бака: "))
diameter = user_input_1

user_input_2 = int(input("Введите высоту бака: "))
height = user_input_2

result = get_tub_volume(diameter, height)
print("Объем =",result, "л")
