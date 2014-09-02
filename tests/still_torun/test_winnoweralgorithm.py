from algorithms.winnoweralgorithm import WinnowerAlgorithm

# test ngrams
def testNgrams():
  algorithm = WinnowerAlgorithm(None)
  tests = [('abcd', 2, [(0, 'ab'), (0, 'bc'), (0 ,'cd')]),
           ('yase\nena', 3, [(0, 'yas'), (0, 'ase'), (0, 'see'), (0, 'een'), (1, 'ena')])]
  for test in tests:
    ngrams=list(algorithm.ngrams(test[0], test[1]))
    print ngrams, test[2]
    assert ngrams == test[2]


def testWindowHashes():
  algorithm = WinnowerAlgorithm(None)
  # result should contain previous results
  tests = [('yaseenhamdulay', [(0, 'aseenha'), (0, 'amdulay')]),
      ('abcdefyaseenhamdulaycdascads', [(0, 'abcdefy'), (0, 'aseenha'), (0, 'amdulay'), (0, 'aycdasc')])]
  for test, expected in tests:
    result = list(algorithm.window_hashes(test, 7))
    assert result == expected

testNgrams()
testWindowHashes()
