class Computer:
    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model
        self.memory = 128

class Display:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resolution = "4K"

class Phone(Display, Computer):
    def print_info(self):
        print(self.model)
        print(self.resolution)
        print(self.memory)
        
phone = Phone(model = "last")
phone.print_info()
