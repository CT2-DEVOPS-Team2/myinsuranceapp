import unittest

from project.persistence.users_dao import *
from flask import jsonify, request

class User_dao_Test(unittest.TestCase):
    def test_get_user(self):
        user = get_user(user_id=2)
        print(user)
        self.assertEqual(user["id"],2)
        self.assertIsNotNone(user["fullname"])
    
    def test_edit_user(self):
        users=get_users()
        #user = request.json
        ok = edit_user("williams", "w@.es", "13-08", "spain", "london", "street1", "12345", 2)
        print(ok)
        self.assertEqual(users[1]["fullname"],"williams")