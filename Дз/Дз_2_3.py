class Employee():
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_salary_info(self):
        print(f"Заробітна плата {self.name} на посаді {self.position}: {self.salary}")

Bob = Employee()