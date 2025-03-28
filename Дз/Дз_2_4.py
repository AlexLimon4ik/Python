class Rectangle:
    def __init__(self, width, heigh):
        self.width = width
        self.height = heigh

    def calculate_area(self):
        self.area = self.width * self.height
        print("Area:", self.area)
        
    def calculate_perimeter(self):
        self.perimeter = 2 * (self.width + self.height)
        print("Perimeter:", self.perimeter)

ABCD = Rectangle(50, 30)

ABCD.calculate_area()
ABCD.calculate_perimeter()