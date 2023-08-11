class Jeans():
    color = ""
    weight = 400
    weight_of_belt = 0
    previous_owner = ""
    amount_of_pockets = 4
    price = 0

    def __init__(self, color, previous_owner, amount_of_pockets, price):
        self.color = color
        self.previous_owner = previous_owner
        self.amount_of_pockets = amount_of_pockets
        self.price = price
    
    def add_belt(self, weight_of_belt):
            self.weight += weight_of_belt
            print(f"Теперь вес с ремнем равен - {self.weight} г")
    
    def add_pockets(self, pockets_to_add):
        self.amount_of_pockets += pockets_to_add
        print(f"Теперь у вас {self.amount_of_pockets} карманов")
    
    def sell_jeans(self, price_to_sell):
        self.price_to_sell = price_to_sell
        print(f"Джинсы проданы за {self.price_to_sell}$")

my_jeans = Jeans("Серый", "No", 5, 150)

my_jeans.add_belt(50)
my_jeans.add_pockets(3)

other_jeans = Jeans("Черный", "Yes", 6, 100)
other_jeans.add_belt(100)
other_jeans.sell_jeans(200)
