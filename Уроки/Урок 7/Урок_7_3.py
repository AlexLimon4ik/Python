def raise_to_the_defrees(number, max_degrees):
    i = 0
    for _ in range(max_degrees):
        yield number**i
        i += 1

res = raise_to_the_defrees(2, 4)
print(res)
for _ in res:
    print(_)