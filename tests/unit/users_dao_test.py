import unittest

from users_dao import users_dao
#from project.persistence.users_dao import get_users
from project.persistence.users_dao import *


class User_dao_Test(unittest.TestCase):
    def get_user(self,user_id):
        user = get_user(id)
        print(user)
