import os
import sys
import unittest
sys.path.append(os.path.dirname(os.path.realpath(__file__))+'/../cheaters')
from algorithms.winnoweralgorithm import WinnowerAlgorithm

class WinnowerAlgorithmTests(unittest.TestCase):

    algorithm = WinnowerAlgorithm(None)

    def test_ngrams(self):
        tests = [('abcd', 2, [(0, 'ab'), (0, 'bc'), (0 ,'cd')]),
                ('yase\nena', 3, [(0, 'yas'), (0, 'ase'), (0, 'see'), (0, 'een'), (1, 'ena')])]
        for test in tests:
            ngrams = list(self.algorithm.ngrams(test[0], test[1]))
            self.failUnless(ngrams == test[2])

    def test_window_hashes(self):
        # result should contain previous results
        tests = [('yaseenhamdulay', [(0, 'aseenha'), (0, 'amdulay')]),
            ('abcdefyaseenhamdulaycdascads', [(0, 'abcdefy'), (0, 'aseenha'), (0, 'amdulay'), (0, 'aycdasc')])]
        for test, expected in tests:
            result = list(self.algorithm.window_hashes(test, 7))
            self.failUnless(result == expected)


if __name__ == '__main__':
    unittest.main()
