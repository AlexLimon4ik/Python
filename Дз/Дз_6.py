people_list = {"Sasha":"young", "Pasha":"adult", "Vladik":"baby", "Oleg":"young", "Kolya":"adult", "Danya":"baby"}

a = input("What is your name: ")

class Error(Exception):
    def __str__(self):
        return f"There is no person with this name."

if a in people_list:
    print(f"Your age group: {people_list[a]}")
else:
    raise Error