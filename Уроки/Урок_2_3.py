class Student():

    height = 160

    def __init__(self):
        self.height = 170
    
    def printer(self):
        print(self.height)

    def change_height(self, new_height):
        self.height = new_height

nick = Student()
nick.printer()
nick.change_height(180)
nick.printer()