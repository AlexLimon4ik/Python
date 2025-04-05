class Human:
    def __init__(self, name="Human"):
        self.name = name
        
class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, *args):
        for human in args:
            self.passengers.append(human)

    def print_passengers_name(self):
        if self.passengers != []:
            print(f"Names of {self.brand} passengers:")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print("There are no passenger")

nick = Human("Nick")
kate = Human("Kate")
car = Auto("Reno Logan")

car.add_passenger(nick, kate)
car.print_passengers_name()