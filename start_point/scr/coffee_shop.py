from scr.customer import Customer

class CoffeeShop:
    def __init__(self, name, till, collection_of_drinks):
        self.name = name
        self.till = till
        self.collection_of_drinks = collection_of_drinks

    def till_increases (self, cash):
        self.till += cash

    def can_buy_drink (self, drink):
        for name_of_drink in self.collection_of_drinks:
            if name_of_drink == drink:
                customer.reducing_wallet (self, )