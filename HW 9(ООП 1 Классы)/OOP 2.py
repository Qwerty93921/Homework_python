class Trainers():
    color = ""
    weight = 550
    color_inside = ""
    years_for_wearing = 3
    previous_owner = ""
    cleanliness_now = ""

    def __init__(self, color, color_inside, previous_owner, cleanliness_now):
        self.color = color
        self.color_inside = color_inside
        self.previous_owner = previous_owner
        self. cleanliness_now = cleanliness_now

    def change_color(self, new_color):
        self.new_color = new_color
        print(f"Теперь цвет кроссовок - {self.new_color}")
    
    def remove_inside_paper(self, paper):
        self.weight -= paper
        print(f"Теперь вес обуви готовой к применению составляет: {self.weight}")
    
    def clean_trainers(self, cleaned):
        self.cleaned = cleaned
        print("Кроссовки теперь чистые")
    
my_trainers = Trainers("красный", "черный", "no", "no")
my_trainers.clean_trainers("yes")

my_trainers.remove_inside_paper(50)
Trainers.color = "Зеленый"
print(Trainers.color)

other_trainers = Trainers("Желтый", "черный", "yes", "yes")
other_trainers.change_color("Фиолетовый")
