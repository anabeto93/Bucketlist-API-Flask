import unittest
import os
import json

#from app import create_app, db
from context import app


class BucketListTestCase(unittest.TestCase):
    '''Testing all functionality for the bucketlist model'''

    def setUp(self):
        '''Define the test env variables and then bootstrap the app.'''
        self.app = app.create_app(config_name='testing')
        self.client = self.app.test_client

        self.bucketlist = {'name': 'Work at Andela'}

        with self.app.app_context():
            #create all the tables as well
            app.db.create_all()

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
        '''Test that API to ensure it can return a bucketlist given the id. (GET request).'''

        #create the bucketlist once again
        res = self.client().post('/bucketlists/', data={'name': 'Work at Google'})
        self.assertEqual(res.status_code, 201) #the bucketlist was created
        res.assertIn('Work at Google', str(res.data))

        json_result = json.loads(res.data.decode('utf-8').replace("'", "\""))
        result = self.client().get(
            '/bucketlists/{}'.format(json_result['id']))

        self.assertEqual(result.status_code, 200)
        self.assertIn('Work at Google', str(result.data))

    def test_bucketlist_is_editable(self):
        '''Test that an existing bucketlist can be edited. (PUT request)'''

        res = self.client().post(
            '/bucketlists',
            data={'name': 'Build an overkill PC'})
        self.assertEqual(res.status_code, 201) #created

        b_data = json.loads(res.data.decode('utf-8').replace("'","\""))

        #edit or update the created bucketlist
        res = self.client().put(
            '/bucketlists/{}'.format(b_data['id']),
            data={'name': 'Build wall mounted PC'}
        )
        self.assertEqual(res.status_code, 200) #update successful

        #get the current or newly created resource
        current = self.client().get('/bucketlists/{}'.format(b_data['id']))
        self.assertIn('Build wall mounted', str(current.data))

    def test_bucketlist_deletion(self):
        '''Test the API that given an id a bucketlist can be deleted. (DELETE request).'''

        #create the resource
        res = self.client().post('/bucketlists/', data={'name': 'Time travel'})
        self.assertEqual(res.status_code, 201) #the bucketlist was created
        res.assertIn('Time travel', str(res.data))

        #delete this absurd bucketlist
        data = json.loads(res.data.decode('utf-8').replace("'", "\""))
        result = self.client().get('/bucketlists/{}'.format(data['id']))
        self.assertEqual(result.status_code, 404) #given id deleted and no longer exists

    def tearDown(self):
        '''teardown all initialized variables.'''
        
        with self.app.app_context():
            app.db.session.remove()
            app.db.drop_all() #drop all tables

if __name__ == '__main__':
    unittest.main()