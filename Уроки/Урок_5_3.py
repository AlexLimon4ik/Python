data = "text"

print(hasattr(data, "replace"))
print(hasattr(data, "reverse"))

print(getattr(data, "startswith"))
print(getattr(data, "startswith", None))
print(getattr(data, "reverse", None))

def first_func():
    pass

print(callable(data))
print(callable(first_func))