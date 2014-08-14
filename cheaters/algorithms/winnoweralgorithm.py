from algorithms.base import BaseAlgorithm

WINDOW_LENGTH = 13
NGRAM_LENGTH = 5

def ngrams(string, ngram_length):
  for i in xrange(len(string)-ngram_length):
    yield string[i:i+ngram_length]

def window_hashes(string):
  ngram_iterator = ngrams(string, NGRAM_LENGTH)
  current_ngrams_hashes = list(hash(ngram_iterator.next()) for i in xrange(NGRAM_LENGTH))
  while ngram_iterator.has_next():
    window_hash = min(current_ngrams_hashes)
    yield window_hash
    current_ngrams_hashes.pop(0)
    curent_ngrams_hashes.push(hash(ngram_iterator.next()))

class WinnowerAlgorithm(BaseAlgorithm):
  ALLOWED_LANGUAGE_EXTENSIONS = ['*']

  def __init__(self):
    self.ngrams = {}

  def isPlagiarised(self, program):
    canonicalised_ = program.canonicalised_program_source

    for h in window_hashes(program.canonicalised_program_source):
      pass
