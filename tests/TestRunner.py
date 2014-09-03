import os
import sys
import glob
import unittest

sys.path.append( os.path.dirname(os.path.realpath(__file__)) +'/../')
sys.path.append( os.path.dirname(os.path.realpath(__file__)) +'/../cheaters/')

class TestRunner:

    def get_test_files(self):
        '''Get all test case files within folder
        @return Array
        '''
        modules = glob.glob(os.getcwd() + '/test_*.py')
        test_files = []
        for file in modules:
            basename = os.path.basename(file)[:-3]
            test_files.append(basename)
        return test_files

    def run(self):
        '''gather all test modules and run them'''
        test_files = self.get_test_files()
        suites = []
        for file in test_files:
            print(file)
            suites.append(unittest.defaultTestLoader.loadTestsFromName(file))
        test_suite = unittest.TestSuite(suites)
        text_runner = unittest.TextTestRunner().run(test_suite)

if __name__ == '__main__':
    t = TestRunner()
    t.run()
