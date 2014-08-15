from algorithms.base import BaseAlgorithm
from collections import deque, defaultdict

WINDOW_LENGTH = 13
NGRAM_LENGTH = 5

'''
given a string and a length generate and return all
length-grams of this string'''
def ngrams(string, ngram_length):
  line_number = 0
  for i in xrange(len(string)-ngram_length):
    if string[i] == '\n':
      line_number += 1
    ngram = linestring[i:i+ngram_length]
    yield (line_number, ngram)


'''
generate all ngrams and then hash the string
'''
def ngrams_hashes(string, ngram_length):
  for line_number, ngram in ngrams(string, ngram_length):
    yield line_number, hash(ngram)


'''
go through every window of length n and choose the minimum
n-gram hash within that window
'''
def window_hashes(string):
  ngram_iterator = ngrams(string, NGRAM_LENGTH)
  ngram_window = deque()
  for i in xrange(ngram_length):
    ngram_window.append(ngram_iterator.next())

  while ngram_iterator.has_next():
    best = min(current_ngrams_hashes, key=lambda x: x[1])
    yield best
    current_ngrams_hashes.popleft()
    ngram_window.append(ngram_iterator.next())


'''
algorithm that implements the winnower search method described
in the MOSS whitepaper
'''
class WinnowerAlgorithm(BaseAlgorithm):
  ALLOWED_LANGUAGE_EXTENSIONS = ['*']

  def __init__(self):
    self.ngrams = defaultdict(list)

  def isPlagiarised(self, program):
    canonicalised_ = program.canonicalised_program_source

    # generate and store all winnower hashes
    program_matches = defaultdict(list)
    for line_number, h in window_hashes(program.canonicalised_program_source):
      if h in self.ngrams:
        for program, match_line_number in self.ngrams[h]:
          program_matches[program].append((line_number, match_line_number))
      self.ngrams[h].append((program, line_number))

    # TODO: look up winnower hashes from other programs and calculate
    # a "matching rating"
