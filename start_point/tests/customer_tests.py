import unittest
from scr.customer import Customer
from scr.drink import Drink
from scr.coffee_shop import CoffeeShop
    
class TestCustomer(unittest.TestCase):
    def setUp (self):
        self.customer = Customer("Charlotte", 10.00)

    def test_customer_has_name (self):
        self.assertEqual ("Charlotte", self.customer.name)

    def test_customer_has_wallet (self):
        self.assertEqual (10.00, self.customer.wallet)

    def test_customer_reducing_wallet (self):
        self.customer.reducing_wallet (3.00)
        self.assertEqual (7.00, self.customer.wallet)

    

