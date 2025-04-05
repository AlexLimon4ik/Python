num1 = 5
num2 = 5.0
string = "Hello"

print(type(num1))
print(type(num2))
print(type(string))

intro_list = []

for method in dir(string):
    print(method)
