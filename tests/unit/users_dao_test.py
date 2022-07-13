import unittest

from project.persistence.users_dao import *


class User_dao_Test(unittest.TestCase):
    def test_get_user(self):
        user = get_user(user_id=2)
        print(user)
        self.assertEqual(user["id"],2)
        self.assertIsNotNone(user["fullname"])

    
