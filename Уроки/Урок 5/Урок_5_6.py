import inspect

class Human:
    def __init__(self, age, height, name="John"):
        self.age = age
        self.height = height
        self.name = name

sig = inspect.signature(Human)
print(sig)
for param in sig.parameters.values():
    print(param.name, param.default)
      