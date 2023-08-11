class Phone():
    memory = ""
    color = ""
    weight = 1
    px_screen = 600
    color_of_case = ""
    amount_of_cameras = 0

    def __init__(self, memory, color, color_of_case, amount_of_cameras):
        self.memory = memory
        self.color = color
        self.color_of_case = color_of_case
        self.amount_of_cameras = amount_of_cameras

    def add_memory_card(self, gb):
        self.memory += gb
        print(f"Размер памяти телефона {self.memory} ГБ")
    
    def change_color(self, new_color):
        self.new_color = new_color
        print(f"Теперь цвет телефона - {self.new_color}")

    def change_color_of_case(self, new_color_of_case):
        self.color_of_case = new_color_of_case
        print(f"Теперь цвет телефона - {self.new_color}")

my_phone = Phone(32, "black", "white", 1)
my_phone.add_memory_card(16)

Phone.color = "gray"
print("Цвет телефона", Phone.color)

other_phone = Phone(64, "зеленый", "желтый", 3)

other_phone.add_memory_card(96)
other_phone.change_color("синий")
