my_list = [1, 2, 3]
iterator = iter(my_list)
print(next(iterator))
print(next(iterator))
print(next(iterator))
try:
    print(next(iterator)) 
except:
    print("4 раз не працює бо в нашому списці немая 4 об'єкту")

    