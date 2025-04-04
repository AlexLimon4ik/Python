class Пристрій:
    def __init__(self):
        pass

    def увімкнути(self):
        self.power = "On"

    def вимкнути(self):
        self.power = "Off"
    
    def print_power(self):
        if self.power == "On":
            print("Пристрій увімкнено")
        else:
            print("Пристрій вимкнено")
    
class Телефон(Пристрій):
    def __init__(self):
        pass

class Ноутбук(Пристрій):
    def __init__(self):
        pass

class Планшет(Пристрій):
    def __init__(self):
        pass

iPad = Планшет()
iMac = Ноутбук()
iPhone = Телефон()

iPad.увімкнути()
iMac.вимкнути()
iPhone.увімкнути()

iPad.print_power()
iMac.print_power()
iPhone.print_power()