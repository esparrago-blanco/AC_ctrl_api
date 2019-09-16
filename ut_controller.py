import os
import controller
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.app = controller.app.test_client()

    def test_api_on_get(self):
        rv = self.app.get('/api/AC/on')
        assert 'The method is not allowed for the requested URL'.encode('utf-8') in rv.data

    def test_api_on_post(self):
        rv = self.app.post('/api/AC/on')
        #print(rv)
        assert 'AC ON!'.encode('utf-8') in rv.data



if __name__ == '__main__':
    unittest.main()
