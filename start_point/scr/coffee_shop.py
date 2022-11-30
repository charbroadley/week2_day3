from scr.customer import Customer

class CoffeeShop:
    def __init__(self, name, till, collection_of_drinks):
        self.name = name
        self.till = till
        self.collection_of_drinks = collection_of_drinks

    def till_increases (self, cash):
        self.till += cash

    def remove_stock(self, drink_selection):
        for drink in self.collection_of_drinks:
            if drink == drink_selection:
                self.collection_of_drinks.remove(drink_selection)
                break

    def sell_drink (self, customer, drink_selection):
        customer.reducing_wallet(drink_selection.price)
        self.till_increases(drink_selection.price)
        self.remove_stock(drink_selection)

