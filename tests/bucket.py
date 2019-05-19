import unittest
import os
import json

from app import create_app, db

class BucketListTestCase(unittest.TestCase):
    '''Testing all functionality for the bucketlist model'''

    def setUp(self):
        '''Define the test env variables and then bootstrap the app.'''
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client

        self.bucketlist = {'name': 'Work at Andela'}

        with self.app.app_context():
            #create all the tables as well
            db.create_all()

    def test_bucketlist_creation(self):
        '''Test the API can create a bucketlist (POST request).'''
        
        res = self.client().post('/bucketlists/', data=self.bucketlist)
        self.assertEqual(res.status_code, 201) #resource created
        self.assertIn('Work At Andela', str(res.data))

    def test_api_can_get_all_bucketlists(self):
        '''Test the API can get all the bucketlists (GET request).'''

        #note that, one test shouldn't affect the next test
        #first create a bucketlist
        res = self.client().post('/bucketlists/', data={'name': 'Learn Ruby on Rails'})
        self.assertEqual(res.status_code, 201) #the bucketlist was created
        res.assertIn('Learn Ruby on Rails', str(res.data))

        #now get the lists of all bucketlists
        res = self.client().get('/bucketlists/')
        self.assertEqual(res.status_code, 200) #no errors
        self.assertIn('Learn Ruby on Rails', str(res.data))

    def test_api_can_get_bucketlist_by_id(self):
        '''Test that API to ensure it can return a bucketlist given the id.'''

        #create the bucketlist once again
        res = self.client().post('/bucketlists/', data={'name': 'Work at Google'})
        self.assertEqual(res.status_code, 201) #the bucketlist was created
        res.assertIn('Work at Google', str(res.data))

        json_result = json.loads(res.data.decode('utf-8').replace("'", "\""))
        result = self.client().get(
            '/bucketlists/{}'.format(json_result['id']))

        self.assertEqual(result.status_code, 200)
        self.assertIn('Work at Google', str(result.data))

    
