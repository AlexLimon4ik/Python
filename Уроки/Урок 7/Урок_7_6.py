def counter(number):
    first_num = number
    def mulitiply(number):
        return first_num**number
    return mulitiply

#first = counter(2)(2)
first = counter(2)
print(first)

print(first(2))
print(first(3))
print(first(4))
print(first(5))
print(first(6))
print(first(7))
print(first(8))


