print(f"NameError - {type(NameError)} - {issubclass(NameError, BaseException)}")

try:
    print("start")
    print(10/0)
    print("no error")
except NameError:
    print("У вас помилка NameError")
except ZeroDivisionError:
    print(" вас помилка ZeroDivisionError")

