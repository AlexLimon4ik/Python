class Product:
    def __init__(self, name, price, index):
        self.name = name
        self.price = price
        self.index = index

class Cart:
    def __init__(self):
        self.products_list = []

    def add_product(self, *args):
        for thing in args:
            self.products_list.append(thing)

    def print_product_names(self):
        if self.products_list != []:
            print("Names of products in cart:")
            for product in self.products_list:
                print(product.name)
        else:
            print("There are nothing in cart")

    def calculate_total_cost(self):
        self.total_price = 0
        for product in self.products_list:
            self.total_price += product.price
        print("Total price:", self.total_price)

    def print_product_indexes(self):
        if self.products_list != []:
            print("Names of products in cart:")
            for product in self.products_list:
                print(product.name,":",product.index)
        else:
            print("There are nothing in cart")  




cart = Cart()

apple = Product("Apple", 5, 1)
potato = Product("Potato", 4, 2)
tomato = Product("Tomato", 3, 3)

cart.add_product(apple, potato, tomato)
cart.print_product_names()
cart.calculate_total_cost()
cart.print_product_indexes()