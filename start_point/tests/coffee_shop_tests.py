import unittest
from scr.coffee_shop import CoffeeShop
from scr.customer import Customer
from scr.drink import Drink

class TestCoffeeShop(unittest.TestCase):
    def setUp (self):
        collection_of_drinks = [{"Name" : "Mocha", "Price" :3.00}, {"Name" : "Tea", "Price" : 2.00}, {"Name" : "Hot Chocolate", "Price" : 4.00}, {"Name" : "Coffee", "Price" : 2.50}]

        self.drink= Drink("Mocha", 3.00)
        self.coffee_shop = CoffeeShop("Kosta Koffee", 100.00)

    def test_coffee_shop_has_name (self):
        self.assertEqual ("Kosta Koffee", self.coffee_shop.name)

    def test_coffee_shop_has_till (self):
        self.assertEqual (100.00, self.coffee_shop.till)
    
    def test_till_increases (self):
        self.coffee_shop.till_increases(10.00)
        self.assertEqual (110.00, self.coffee_shop.till)

    def 

    def test_customer_can_buy_drink (self):
        drink_1 = Drink ("Mocha", 3.00)
        Customer.reducing_wallet (drink_1)
        CoffeeShop.till_increases (drink_1)
        self.buy_drink (customer, drink_selection)
        self.assertEqual(7.00, Customer.wallet)
        self.assertEqual(103.00, CoffeeShop.till)
        