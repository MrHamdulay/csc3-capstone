import os
import sys
import unittest
sys.path.append(os.path.dirname(os.path.realpath(__file__))+'/../cheaters')
from languages.python import PythonLanguageHandler

class PythonCanonicalisationTest(unittest.TestCase):

    code = '''
    print 'hello world'

    class A:
    def first_function(self, a):
        a *= 2
        if isinstance(a, int):
        print 'This most definitely gets executed for sure'

        return first_function

    def second_function(b):
    b = 2
    for i in xrange(1000):
        first_function(i)
        b = 2
        for i in xrange(1000):
        first_function(i)

    b = 2
    for i in xrange(1000):
    first_function(i)'''

    expected='''print 's'

    class A:
        def f(i, i):
            i *= 2
            if i(i, i):
                print 's'

            return i

    def f(i):
        i = 2
        for i in i(1000):
            i(i)
            i = 2
            for i in i(1000):
                i(i)

    i = 2
    for i in i(1000):
        i(i)'''

    def test_renamer_transform(self):
        # not sure how to test
        return

    def test_python_language_handler(self):
        '''
        py_language_handler = PythonLanguageHandler(self.code)
        py_language_handler.parse_file()
        source = program.get_canonicalised_program_source.strip()
        self.failUnless(source == self.expected.strip())
        '''
        # i wasn't sure what to do here
        return



if __name__ == '__main__':
    unittest.main()
