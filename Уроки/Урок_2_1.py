class Student():
    height = 160
    def __init__(self):
        print(self.height)
        self.height += 10
        print(self.height)

nick = Student()
kate = Student()