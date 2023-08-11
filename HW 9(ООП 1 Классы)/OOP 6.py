class Tree():
    height = 0
    width = 0
    weight = 0
    amount_of_branches = 0
    color_of_wood = ""
    age = 0

    def __init__(self, height, width, weight, amount_of_branches, color_of_wood, age):
        self.height = height
        self.width = width
        self.weight = weight
        self.amount_of_branches = amount_of_branches
        self.color_of_wood = color_of_wood
        self.age = age
    
    def cut_the_branches(self, kg_of_branches):
        self.weight -= kg_of_branches
        self.amount_of_branches = 0
        print(f"Вес дерева без веток = {self.weight} кг, веток на дереве - {self.amount_of_branches}")
    
    def paint_the_tree(self, color_of_paint):
        self.color_of_paint = color_of_paint
        self.color_of_wood = color_of_paint
        print(f"Цвет дерева - {self.color_of_paint}")

    def wait_years(self, years_to_wait):
        self.years_to_wait = years_to_wait
        self.age += years_to_wait
        print(f"Дереву теперь {self.age} лет")


my_tree = Tree(10, 2, 50, 30, "Коричневый", 15)
print(my_tree.color_of_wood)

my_tree.paint_the_tree("Серый")
my_tree.wait_years(5)

other_tree = Tree(20, 3, 80, 60, "Коричневый", 30)
other_tree.wait_years(10)

other_tree.cut_the_branches(15)

other_tree.paint_the_tree("Белый")
