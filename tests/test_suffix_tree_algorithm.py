import os
import sys
import unittest
sys.path.append(os.path.dirname(os.path.realpath(__file__))+'/../cheaters')
from languages.python import PythonLanguageHandler
from model.submissions import Submission
from algorithms.suffixtreealgorithm import SuffixTreeAlgorithm



class SuffixTreeAlgorithmTestCase(unittest.TestCase):
    def test_comparison(self):
        st=SuffixTreeAlgorithm()
        submissions=[Submission(1, 'hmdyas001',

'''c=0
print 'hello'
for i in range(1000):
    stuff()
    more_things(213, '')
''',

1, 1, 'py'),
Submission(2, 'lllmer001',

'''z=0
i=0
print 'asdf'
for j in range(1000):
    stuff()
    more_things(21, 'things')
''',

1, 1, 'py')]
        matches = st.calculate_document_similarity(*submissions)
        self.assertEqual(str(matches), '[[<Match their_submission_id:1 my_start_line:0 match_length:4 (0)>], [<Match their_submission_id:2 my_start_line:1 match_length:4 (0)>]]')

    def test_wrap_to_lines(self):
#            0123456789  12
        a = '   hello my \nname is\n yaseen'
        st=SuffixTreeAlgorithm()
        self.assertEqual(st.wrap_substring_to_lines(a, 6, len(a)-3), (12, 20))
        self.assertEqual(st.wrap_substring_to_lines(a, 6, len(a)), (12, len(a)))
        self.assertEqual(st.wrap_substring_to_lines(a, 2, len(a)), (2, len(a)))

    def test_partial_lines(self):
        submissions=[Submission(1, 'hmdyas001',

'''
print 'a'
print 'a'
print 'a'
print 'a'
print 'a'
print 'a'
a = asdfs.asdfasd()
print 'a'
print 'a'
print 'a'
''',

1, 1, 'py'),
Submission(2, 'lllmer001',

'''
print 'a'
print 'a'
print 'a'
print 'a'
print 'a'
print 'a'
b = 'asdfjakldsfjkalsdjfklasdjfl'
print 'a'
print 'a'
print 'a'
''',

1, 1, 'py')]
        matches = SuffixTreeAlgorithm().calculate_document_similarity(*submissions)
        print str(matches)

if __name__ == '__main__':
    unittest.main()
