import unittest

from project.persistence.users_dao import *


class User_dao_Test(unittest.TestCase):
    def test_get_user(self):
        user = get_user(user_id=2)
        print(user)
        self.assertEqual(user["id"],2)
        self.assertIsNotNone(user["fullname"])
    
    def test_edit_user(self):
        users=get_users()
        print(users)
        ok = edit_user("williams", "w@.es", "13-08", "spain", "london", "street1", "12345", 2)
        print(ok)
        self.assertEqual(users[1]["fullname"],"williams")
        
    def test_createUser(self):

        newuser=create_user("Usuario nuevo", "suario@.es","13-07-2022", "pais 1","ciudad 1"," avenue1","pw")
        print(newuser)
        #hacer validacion si el metodo es true.. si es true quiere decir que esta bien
        self.assertTrue(newuser)
