import unittest
from scr.coffee_shop import CoffeeShop
from scr.customer import Customer
from scr.drink import Drink

class TestCoffeeShop(unittest.TestCase):
    def setUp (self):
        self.drink1= Drink("Mocha", 3.00)
        self.drink2= Drink("Tea", 2.50)
        self.drink3= Drink("coffee", 2.00)
        self.drink4= Drink("Hot chocolate", 4.00)
        collection_of_drinks = [self.drink1, self.drink2, self.drink3, self.drink4]
        self.coffee_shop = CoffeeShop("Kosta Koffee", 100.00, collection_of_drinks)
        

    def test_coffee_shop_has_name (self):
        self.assertEqual ("Kosta Koffee", self.coffee_shop.name)

    def test_coffee_shop_has_till (self):
        self.assertEqual (100.00, self.coffee_shop.till)
    
    def test_till_increases (self):
        self.coffee_shop.till_increases(10.00)
        self.assertEqual (110.00, self.coffee_shop.till)
    
    def test_remove_drink_by_name(self):
        self.coffee_shop.remove_stock(self.drink1)
        self.assertEqual (3,len(self.coffee_shop.collection_of_drinks))

    def test_shop_sells_drink (self):
        customer = Customer("Charlotte", 10.00)
        self.coffee_shop.sell_drink(customer, self.drink1)
        self.assertEqual(7.00, customer.wallet)
        self.assertEqual(103.00, self.coffee_shop.till)
        self.assertEqual(3, len(self.coffee_shop.collection_of_drinks))


        