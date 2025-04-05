
try:
    print("start")
    print(10/0)
    print("no error")
except (NameError, ZeroDivisionError) as error:
    print(f"У вас помилка {error}")

try:
    try:
        print("start")
        print(error)
        print("no error")
    except SyntaxError:
        print("Wrong Syntax")
except NameError as error:
    print(error)
    