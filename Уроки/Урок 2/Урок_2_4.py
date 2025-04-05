class Student:

    def __init__(self, name=None, height=160):
        self.name = name
        self.height = height

    def __bool__(self):
        return self.name != None # != is not
    
    def __len__(self):
        return self.height
    
    def __del__ (self):
        print("Студент все...")

nick = Student()
print(nick.__bool__())
print(nick.__len__())
print(len(nick))
print(bool(nick))
