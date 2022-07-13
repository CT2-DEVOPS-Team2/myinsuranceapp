
import json
import unittest
from project import app
import project


class TestApp(unittest.TestCase):
    token=''

    def test_1_post_(self):
        route = app.test_client(self)
        response = route.post('/api/v1/users/', content_type='application/json')
        data = json[response.text]
        print(f"get post: {data}")
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(data, [0])

    def test_2_post(self):
        tester = app.test_client(self)
        test_data = {"address": "C Street 1",
                     "email": "jd@myinsuranceapp.com",
                     "fullname": "John Doe"}
        response = tester.post('/api/v1/users/',content_type='application/json', json=test_data)
        data=json.loads(response.text)
        print(f"post: {data}")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data[0]['id'])

    def test_3_get_none(self):
        tester = app.test_client(self)
        response = tester.post('/api/v1/token', content_type='application/json')
        data=json.loads(response.text)
        print(f"get post 2: {data}")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(data)>0)
