from pyperclip import copy

def cope(message):
    c = []
    b = 0
    for string in range(0, 10000):
        b += 1
        c.append(f"{b}. {message}")  
    return c

inp = input("Message: ")
a = cope(inp)

copy(a)
