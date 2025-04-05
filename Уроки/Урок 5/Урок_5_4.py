class First:
    pass

class Second(First):
    pass

print(issubclass(First, Second))
print(issubclass(Second, First))

obj = Second()

print(isinstance(obj, Second))
print(isinstance(obj, First))