import os
import sys
import unittest
from flask import Flask

class ServerTests(unittest.TestCase):

    def test_index_route(self):
        ''' ensure @route('/') returns 200 response code'''
        client = app.test_client()
        resp = client.get('/')
        self.failUnless(resp.status_code == 200)


def main():
    unittest.main()

if __name__ == '__main__':
    sys.path.append(os.path.dirname(os.path.realpath(__file__))+'/../server')
    from server import View
    app = Flask('server')
    View.register(app)
    main()
