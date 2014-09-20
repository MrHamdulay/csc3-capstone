import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__))+'/../cheaters/')
from algorithms.suffix_tree import SuffixTree


class SuffixTreeTest(unittest.TestCase):
    """Some functional tests.
    """
    def test_empty_string(self):
        st = SuffixTree('')
        self.assertEqual(st.find_substring('not there'), -1)
        self.assertEqual(st.find_substring(''), -1)
        self.assertFalse(st.has_substring('not there'))
        self.assertFalse(st.has_substring(''))

    def test_repeated_string(self):
        st = SuffixTree("aaa")
        self.assertEqual(st.find_substring('a'), 0)
        self.assertEqual(st.find_substring('aa'), 0)
        self.assertEqual(st.find_substring('aaa'), 0)
        self.assertEqual(st.find_substring('b'), -1)
        self.assertTrue(st.has_substring('a'))
        self.assertTrue(st.has_substring('aa'))
        self.assertTrue(st.has_substring('aaa'))

        self.assertFalse(st.has_substring('aaaa'))
        self.assertFalse(st.has_substring('b'))
        #case sensitive by default
        self.assertFalse(st.has_substring('A'))

    def test_long_string(self):
        f = open("test.txt")
        st = SuffixTree(f.read())
        self.assertEqual(st.find_substring('Ukkonen'), 1498)
        self.assertEqual(st.find_substring('Optimal'), 11131)
        self.assertFalse(st.has_substring('ukkonen'))

    def test_case_sensitivity(self):
        f = open("test.txt")
        st = SuffixTree(f.read(), case_insensitive=True)
        self.assertEqual(st.find_substring('ukkonen'), 1498)
        self.assertEqual(st.find_substring('Optimal'), 1830)

    def test_lcs(self):
        st = SuffixTree(['yaseen hamdulay is a something something',
            'aalia hamdulay likes maths sometimes'])
        self.assertEqual(st.longest_common_substring(), ' hamdulay ')

        st = SuffixTree(['aaa\naaa', 'aaa\n\naaa'])
        self.assertEqual(st.longest_common_substring(), ['aaa\naaa'])

    def test_long_strings(self):
        st = SuffixTree(['abcdefghijkl', 'z;kdiowghijklabc12'])
        self.assertEqual(list(st.common_substrings_longer_than(3)), ['abc', 'ghijkl', 'ijkl', 'hijkl', 'jkl'])
        st = SuffixTree(['aaaaaaaa', 'aaa'])
        self.assertEqual(list(st.common_substrings_longer_than(2)), ['aaa'])

    def test_repr(self):
        st = SuffixTree("t")
        output = '\tStart \tEnd \tSuf \tFirst \tLast \tString\n\t0 \t1 \t-1 \t0 \t0 \tt\n'
        #import pdb;pdb.set_trace()
        self.assertEqual(st.__repr__(), output)

if __name__ == '__main__':
    unittest.main()

