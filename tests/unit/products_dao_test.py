import unittest
from project.persistence.products_dao import *

class TestProducts(unittest.TestCase):

    def test_1_get_product(self):
        product = get_products()
        print(product["name"])
        #self.assertEqual(self.products.name,"Property & Casualty Insurance")

        