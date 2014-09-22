import os
import sys
import unittest
sys.path.append(os.path.dirname(os.path.realpath(__file__))+'/../cheaters')
from languages.python import PythonLanguageHandler
from model.submissions import Submission
from algorithms.suffixtreealgorithm import SuffixTreeAlgorithm

submissions1=[Submission(1, 'hmdyas001',

'''c=0



print 'hello'
for c in range(1000):
    stuff()
    more_things(21, j)
''',

1, 1, 'py'),
Submission(2, 'lllmer001',

'''z=0
i=0
print 'asdf'
for i in range(1000):
    stuff()
    more_things(21, j)
z=0
i=0
print 'asdf'
for i in range(1000):
    stuff()
    more_things(21, j)
''',

1, 1, 'py')]

submissions2=[Submission(1, 'hmdyas001',

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


class SuffixTreeAlgorithmTestCase(unittest.TestCase):
    def test_string_index_to_line_numbers(self):
        st=SuffixTreeAlgorithm()
        l=st.string_indexes_to_line_numbers('a \nb\nc\n def\ng')
        l.send(None)
        self.assertEqual((0, 1), l.send((1, 3)))
        self.assertEqual((0, 1), l.send((1, 3)))
        self.assertEqual((2, 3), l.send((5, 9)))

    def test_variable_matching(self):
        st=SuffixTreeAlgorithm()
        self.assertTrue( st._variable_match('a=0; b=0; c=a', 'z=0; x=0; v=z'))
        self.assertFalse(st._variable_match('a=0; b=0; c=a', 'z=0; y=0; z=x'))
        self.assertFalse(st._variable_match('a=0; print a', 'a=0; print b'))
        self.assertTrue(st._variable_match('a=0; b=0; print a', 'a=0; b=0; print a'))

    def test_comparison(self):
        st=SuffixTreeAlgorithm()
        matches = st.calculate_document_similarity(*submissions1)
        self.assertEqual(str(matches), '[[<Match their_submission_id:1 my_start_line:0 match_length:7 (0)>],'
                                       ' [<Match their_submission_id:2 my_start_line:1 match_length:4 (0)>,'
                                        ' <Match their_submission_id:2 my_start_line:7 match_length:4 (0)>]]')

    def test_wrap_to_lines(self):
#            012  345678  9  12
        a = 'hel\nnameis\nyaseen'
        st=SuffixTreeAlgorithm()
        string, lines = st.whitespaced_stripped_with_line_numbers(a)
        self.assertEqual(st.wrap_substring_to_lines(string, lines, 0, 2), (0, 2))
        self.assertEqual(st.wrap_substring_to_lines(string, lines, 0, 5), (0, 2))
        self.assertEqual(st.wrap_substring_to_lines(string, lines, 1, 13), (3, 8))
        self.assertEqual(st.wrap_substring_to_lines(string, lines, 8, 15), (9, 15))

    def test_partial_lines(self):
        matches = SuffixTreeAlgorithm().calculate_document_similarity(*submissions2)
        self.assertEqual(str(matches), '[[<Match their_submission_id:1 my_start_line:1 match_length:5 (0)>],'
                                       ' [<Match their_submission_id:2 my_start_line:1 match_length:5 (0)>]]')
#                                      '[[<Match their_submission_id:1 my_start_line:1 match_length:5 (0)>],
#                                        [<Match their_submission_id:2 my_start_line:1 match_length:5 (0)>]]

if __name__ == '__main__':
    unittest.main()
