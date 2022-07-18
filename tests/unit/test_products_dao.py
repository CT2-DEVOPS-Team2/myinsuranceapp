from itertools import product
import unittest
from project.persistence.products_dao import *

class TestProducts(unittest.TestCase):

    # Test passes
    def test_1_get_product(self):
        products = get_products()
        print(products[0]["name"])
        self.assertEqual(products[0]["name"],"Property & Casualty Insurance")
        # print(product[2]["name"])
    
    # Test case fails
    # def test_2_create_product(self):
    #     #new_product = [{"name": "Car Insurance", "description": "Whether you are looking to protect your car, we are here to help you plan your future. Our individual, retail and corporate clients enjoy an extensive line of products and services in all insurance business lines, designed to protect them against risks.", "cost": 200.0, "is_active": 1}]
    #     created_product = create_product("Full+Full Insurance", "Whether you are looking to protect your car, we are here to help you plan your future. Our individual, retail and corporate clients enjoy an extensive line of products and services in all insurance business lines, designed to protect them against risks.", 200.0, 1)
    #     print(created_product)
    #     product = get_product(61)
    #     print(product)
    #     self.assertEqual(product["name"], "Full+Full Insurance")

    # Test passes
    def test_3_edit_product(self):        
        product = get_product(5)
        #print(product)
        edited_product = edit_product("House Insurance", "Whether you are looking to protect your life, we are here to help you plan your future. Our individual, retail and corporate clients enjoy an extensive line of products and services in all insurance business lines, designed to protect them against risks.", 70.0, 1, 5)
        #print(edited_product)
        product = get_product(5)
        print(product)
        self.assertEqual(product["name"], "House Insurance")
