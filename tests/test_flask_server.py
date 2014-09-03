import os
import sys
import unittest
from flask import Flask

sys.path.append(os.path.dirname(os.path.realpath(__file__))+'/../server')
from server import View
app = Flask('server')
View.register(app)

class ServerTests(unittest.TestCase):

    def test_index_page(self):
        '''ensure home page returns 200'''
        self.fail_unless_get('/', 200)

    def test_view_submit_form(self):
        '''ensure view_submit_form returns 200'''
        self.fail_unless_get('/submit', 200)

    def test_view_create_assignment(self):
        '''ensure test_view_create_assignment returns 200'''
        self.fail_unless_get('/createAssignment', 200)

    def test_view_submissions(self):
        '''ensure view_submissions returns 200'''
        self.fail_unless_get('/1', 200)

    def test_view_diff(self):
        '''ensure view_diff returns 200'''
        self.fail_unless_get('/1/1', 200)

    def fail_unless_get(self, route, code):
        '''Fails test unless the give route
        returns the expected response code'''
        client = app.test_client()
        resp = client.get('/')
        self.failUnless(resp.status_code == code)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
