def raise_to_the_defrees(num, max):
    i = 0
    for _ in range(max):
        yield num**i
        i += 1

a = raise_to_the_defrees(2, 100)

for _ in a:
    print(_)