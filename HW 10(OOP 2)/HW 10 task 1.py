import random
from datetime import datetime, timedelta

class Person:

    def __init__(self, name, iin):
        self.name = name
        self.iin = iin
        self.order = None

class Order:

    def __init__(self, hotel_name, room, date_from, date_to, visitor_name, visitor_iin):
        self.hotel_name = hotel_name
        self.id = random.randint(1000, 9999)
        self.room = room
        self.date_from = date_from
        self.date_to = date_to
        self.visitor_name = visitor_name
        self.visitor_iin = visitor_iin
    
    def show_info(self):
        print(f"ID заказа: {self.id}")
        print(f"Отель: {self.hotel_name}")
        print(f"Комната: {self.room.number}")
        print(f"С какого числа заселение: {self.date_from}")
        print(f"С какого числа выселение: {self.date_to}")
        print(f"Visitor: {self.visitor_name} (IIN: {self.visitor_iin})")

class Room:

    def __init__(self, number, bedrooms):
        self.number = number
        self.bedrooms = bedrooms
        self.order = None
    
    def is_empty(self, date=None):
        if not date:
            date = datetime.now().date()
        if self.order and self.order.date_from <= date <= self.order.date_to:
            return False
        return True
    
    def show_info(self):
        print(f"Номер комнаты: {self.number}")
        print(f"Количество спален: {self.bedrooms}")
        if self.order:
            print(f"Забронировано с {self.order.date_from} по {self.order.date_to}")
            print(f"Гость: {self.order.visitor_name} \n (ИИН: {self.order.visitor_iin})")
        else:
            print("Комната свободна")

class Hotel:
    
    def __init__(self, name, balance, room_count):
        self.name = name
        self.balance = balance
        self.rooms = [Room(number, 2 if number % 2 == 0 else 1) for number in range(1, room_count + 1)]
    
    def get_price(self, room_number, date_from, date_to):
        room = self.rooms[room_number - 1]
        price_per_bedroom = 100 if room.bedrooms == 1 else 150
        days = (date_to - date_from).days
        return price_per_bedroom * room.bedrooms * days
    
    def buy_order(self, bedrooms, date_from, date_to, visitor):
        empty_rooms = [room for room in self.rooms if room.is_empty(date_from)]
        available_rooms = [room for room in empty_rooms if room.bedrooms == bedrooms]
        if available_rooms:
            room = available_rooms[0]
            price = self.get_price(room.number, date_from, date_to)
            if self.balance >= price:
                self.balance -= price
                order = Order(self.name, room, date_from, date_to, visitor.name, visitor.iin)
                room.order = order
                visitor.order = order
                print("Заказ сделан")
            else:
                print("Недостаточно денег на счету чтобы сделать заказ")
        else:
            print("Нет доступных комнат на выбранный период времени")
    
    def check_in(self, visitor, date):
        if visitor.order and visitor.order.room.is_empty(date) and visitor.order.date_to >= date:
            print("Заселение успешно пройдено")
        else:
            print("Процедура заселения не может быть завершена. Не действительный заказ")
    
    def check_out(self, visitor, date):
        if visitor.order and visitor.order.date_to <= date:
            extra_days = (date - visitor.order.date_to).days
            price = self.get_price(visitor.order.room.number, visitor.order.date_from, date)
            if extra_days > 0:
                price += 50 * extra_days
            self.balance += price
            print(f"Выселение прошло успешно. Ваш счет: {price}")
            visitor.order.room.order = None
            visitor.order = None

hotel = Hotel("Hotel 123", 5000, 20)

visitor = Person("Ivan Ivanov", "123456789012")

hotel.buy_order(2, datetime.now().date(), (datetime.now() + timedelta(days=5)).date(), visitor)

hotel.check_in(visitor, datetime.now().date())

hotel.check_out(visitor, (datetime.now() + timedelta(days=6)).date())

room = hotel.rooms[0]
room.show_info()
if room.order:
    room.order.show_info()
