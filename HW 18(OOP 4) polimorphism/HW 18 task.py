class Animal():
    name = ""
    weight = 0
    size = 0

    def __init__(self, name, weight, size):
        self.name = name
        self.weight = weight
        self.size = size
    
    def talk(self):
        print("Mmmmmmm...")
    
    def eat(self, meal):
        len_of_meal = len(meal)
        self.size += len_of_meal
        self.weight += len_of_meal
    
class Herbivore(Animal):
    def __init__(self, name, weight, size, ratio):
        super().__init__(name, weight, size)
        self.ratio = []

    def eat(self, meal):
        if self.meal in self.ratio:
            self.weight += len(meal)
            self.size += len(meal)
        else:
            print("Еда не подходит для травоядного")
    
class Predator(Animal):
    def __init__(self, name, weight, size):
        super().__init__(name, weight, size)
    
    def eat(self, meal):
        if self.meal == Herbivore and self.weight > Herbivore.weight and self.size > Herbivore.size:
            self.weight += len(meal) * 0.2
            self.size += len(meal) * 0.2
        else:
            print("Животное слишком крупное чтобы его есть")

class Goose(Herbivore):
    def __init__(self, name, weight, size, ratio):
        super().__init__(name, weight, size, ratio)

    def talk(self, amount_of_ga):
        print(f"Гусь сказал ГА {self.amount_of_ga} раз")
    
    def fly(self, fly_height):
        print(f"Гусь взлетел на {self.fly_height} метров вверх")

class Wolf(Predator):
    def __init__(self, name, weight, size):
        super().__init__(name, weight, size)

    def howl(self, time_of_howl_in_seconds):
        print(f"Волк воет на луну в течении {self.time_of_howl_in_seconds} секунд")
