class Counter():
    def __init__(self, max_number):
        self.i = 0
        self.max_number = max_number
    def __iter__(self):
        self.i = 0
        return self
    def __next__(self):
        self.i += 1
        if self.i > self.max_number:
            raise StopIteration 
        return self.i
    
insert_num = int(input("Введіть максимальне число: "))

count = Counter(insert_num)
for elem in count:
    print(elem)