class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        print(f"Year:{self.year} Make:{self.make} Model:{self.model}")

Grandpas_Car = Car("Mercedes", "CDI","2012")

Grandpas_Car.get_info()