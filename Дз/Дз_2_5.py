class Product():
    def __init__(self, name, price, quantity):
        self.name = name 
        self.price = price 
        self.quantity = quantity

    def canculate_total_price(self):
        self.total_price = self.price * self.quantity
        print(self.total_price)
    
    def display_info(self):
        print(f"Назва:{self.name} Ціна:{self.price} Кількість:{self.quantity}")

Toy = Product("Машинка", 5, 40)

Toy.canculate_total_price()
Toy.display_info()