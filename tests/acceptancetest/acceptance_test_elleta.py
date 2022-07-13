import json
import unittest
from project import web
import project


class TestWeb(unittest.TestCase):
    token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1NzY5ODM0NywianRpIjoiMTMyMDQwODgtMGUzZi00NjgwLWFhY2QtMzU5NDJhNmRlYjlkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjU3Njk4MzQ3LCJleHAiOjE2NTc2OTkyNDd9.hcUUMKI_r3L77kiKmgUSA9R0llLor4og6lX0uFWGWWE'

    def test_1_get_none(self):
        tester = project.test_client(self)
        response = tester.get('/api/v1/customers/', content_type='application/json')
        data=json.loads(response.text)
        print(f"get 1: {data}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, [])

    def test_2_post(self):
        tester = project.test_client(self)
        test_data = {"address": "5 Spenser Plaza",
                     "email": "kbraksper0@mac.com",
                     "name": "Kelbee"}
        response = tester.post('/api/v1/customers/',content_type='application/json', json=test_data)
        data=json.loads(response.text)
        print(f"post: {data}")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['id'] != None)

    def test_3_get_none(self):
        tester = project.test_client(self)
        response = tester.get('/api/v1/customers/', content_type='application/json')
        data=json.loads(response.text)
        print(f"get 2: {data}")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(data)>0)

    def test_4_testToken(self):
        tester = project.test_client(self)
        test_data = {"email":"user@test.com","password":"passwordjd"}
        response = tester.post('/api/v1/token',content_type='application/json', json=test_data)        
        data=json.loads(response.text)
        print(f"post token: {data}")
        self.assertEqual(response.status_code, 200)
        if response.status_code==200:
            TestWeb.token=data['token']
        
    def test_5_get_restricted(self):
        tester = project.test_client(self)
        print(f"token: {self.token}")
        headers = {"Authorization": f"Bearer {TestWeb.token}"}

        response = tester.get('/api/v1/restricted', content_type='application/json', headers=headers)
        data=json.loads(response.text)
        print(f"get restricted: {data}")
        self.assertEqual(response.status_code, 200)
