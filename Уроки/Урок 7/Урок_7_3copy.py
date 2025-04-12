def raise_to_the_defrees(number):
    i = 0
    while True:
        result = number**i
        if result > 100**20:
            return
        i += 1

res = raise_to_the_defrees(2)
print(res)

for _ in res:
    print(_)