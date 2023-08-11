class Bottle():
    volume = 0
    current_litres = 0
    color_of_bottle = ""
    color_of_liquid = ""
    sparkling = ""
    harmful_drink = ""

    def __init__(self, volume, current_litres, color_of_bottle, color_of_liquid, sparkling, harmful_drink):
        self.volume = volume
        self.current_litres = current_litres
        self.color_of_bottle = color_of_bottle
        self.color_of_liquid = color_of_liquid
        self.sparkling = sparkling
        self.harmful_drink = harmful_drink
    
    def fill(self, liters):
        if self.current_litres + liters >= self.volume:
            self.current_litres = self.volume
        else:
            self.current_litres += liters
    
    def pour_out(self, liters_outside):
        if liters_outside >= self.current_litres:
            self.current_litres = 0
            print(f"Теперь бутылка пустая, запас = {self.current_litres} л")
        else:
            self.current_litres -= liters_outside
            print(f"Теперь в бутылке {self.current_litres} л")
    
    def add_paint_to_liquid(self, color_of_paint):
        self.color_of_paint = color_of_paint
        print(f"Теперь цвет жидкости - {self.color_of_paint}")
    
    def paint_the_bottle(self, new_color_of_bottle):
        self.new_color_of_bottle = new_color_of_bottle
        print(f"Теперь цвет бутылки - {self.new_color_of_bottle}")
    
my_bottle = Bottle(3, 1, "Красный", "Прозрачный", "Yes", "No")
my_bottle.fill(5)
print(my_bottle.current_litres, "л")

my_bottle.pour_out(10)
print(my_bottle.current_litres, "л")

my_bottle.add_paint_to_liquid("Синий")

other_bottle = Bottle(15, 5, "Белый", "Прозрачный", "No", "No")
other_bottle.paint_the_bottle("Черный")
