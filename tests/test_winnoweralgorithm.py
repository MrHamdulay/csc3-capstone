from algorithms.winnoweralgorithm import WinnowerAlgorithm

# test ngrams
def testNgrams():
  algorithm = WinnowerAlgorithm()
  tests = [('abcd', 2, [(0, 'ab'), (0, 'bc'), (0 ,'cd')]),
           ('yase\nen', 3, [(0, 'yas'), (0, 'ase'), (0, 'se\n'), (0, 'e\ne'), (1, '\nen')])]
  for test in tests:
    ngrams=list(algorithm.ngrams(test[0], test[1]))
    assert ngrams == test[2]


def testWindowHashes():
  algorithm = WinnowerAlgorithm()
  # result should contain previous results
  tests = [('yaseenhamdulay', [(0, 'aseenha'), (0, 'amdulay')]),
      ('abcdefyaseenhamdulaycdascads', [(0, 'abcdefy'), (0, 'aseenha'), (0, 'amdulay'), (0, 'aycdasc')])]
  for test, expected in tests:
    result = list(algorithm.window_hashes(test, 7))
    assert result == expected

testNgrams()
testWindowHashes()
print 'ALL PASSED :D'
