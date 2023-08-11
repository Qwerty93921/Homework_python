class Pen():
    color_of_pen = ""
    color_of_paste = ""
    weight = 10
    length = 7
    current_paste = 0
    volume = 0

    def __init__(self, color_of_pen, color_of_paste, volume):
        self.color_of_pen = color_of_pen
        self.color_of_paste = color_of_paste
        self.volume = volume

    def paste_refuel(self, grams_of_paste):
        if self.current_paste + grams_of_paste >= self.volume:
            self.current_paste = self.volume
            print(f"Запас пасты полон - {self.current_paste} грамм")
        else:
            self.current_paste += grams_of_paste

    def change_color_of_paste(self, new_color_of_paste):
        self.new_color_of_paste = new_color_of_paste
        print(f"Теперь цвет пасты - {self.new_color_of_paste}")
    
    def paint_the_pen(self, new_color_of_pen):
        self.new_color_of_pen = new_color_of_pen
        print(f"Теперь цвет ручки - {self.new_color_of_pen}")
    
my_pen = Pen("Зеленый", "Синий", 100)
my_pen.paste_refuel(50)
print(my_pen.current_paste, "грамм пасты")

my_pen.change_color_of_paste("Красный")

other_pen = Pen("Черная", "желтая", 200)
other_pen.paste_refuel(250)

other_pen.paint_the_pen("Фиолетовый")
