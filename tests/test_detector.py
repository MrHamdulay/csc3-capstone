import os
import sys
import unittest
sys.path.append(os.path.dirname(os.path.realpath(__file__))+'/../cheaters')
from detector import Detector

class TestDetector(unittest.TestCase):

    def test_overlapping_ranges(self):
        ranges=[(5, 8), (1, 7), (-10, -5), (9, 10), (1, 2), (-11, -10)]
        removed = Detector.remove_overlapping_ranges(ranges)
        self.assertEqual(removed, [(-11, -5), (1, 8), (9, 10)])

    def test_string_indexes_to_line_numbers(self):
        #    012 34567 89
        s = 'abc\ndefg\nhij'
        queries = [(4, 9), (1, 4), (2, 9)]
        expected = [(1, 2), (0, 1), (0, 2)]
        self.assertEqual(Detector.string_indexes_to_line_numbers(s, queries), expected)


if __name__ == '__main__':
    unittest.main()
