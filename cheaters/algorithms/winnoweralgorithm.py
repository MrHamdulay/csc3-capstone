import hashlib

from algorithms.base import BaseAlgorithm, SectionMatch
from model.signature import Signature
from collections import deque, defaultdict

WINDOW_LENGTH = 13
NGRAM_LENGTH = 8

hash_function = lambda s: int(hashlib.sha1(s).hexdigest(), 16)

'''
algorithm that implements the winnower search method described
in the MOSS whitepaper
'''
class WinnowerAlgorithm(BaseAlgorithm):
  ALLOWED_LANGUAGE_EXTENSIONS = ['*']
  MINIMUM_SIGNATURES_MATCH_THRESHOLD = 5

  language_handler = None


  def __init__(self, language_handler):
    self.current_ngrams = defaultdict(list)
    self.language_handler = language_handler

  def generate_signatures(self):
    stripped_source = self.language_handler.strip_unstable_atrributes()

    # generate, store and look up all winnower hashes
    signatures = []
    for line_number, hash in self.window_hashes(stripped_source):
        signatures.append(Signature(hash, None, line_number))

    return signatures

  def whitespaced_stripped_with_line_numbers(self, string):
      WHITESPACE = ' \n\t'
      line_number = 0
      for char in string:
          if char == '\n':
              line_number += 1
          if char in WHITESPACE:
              continue
          yield line_number, char

  '''
  given a string and a length generate and return all
  length-grams of this string'''
  def ngrams(self, string, ngram_length):
    line_number = 0
    string = list(self.whitespaced_stripped_with_line_numbers(string))
    last_ngram = None
    for i in xrange(len(string)-ngram_length+1):
        ngram_pairs = string[i:i+ngram_length]
        ngram = (ngram_pairs[0][0], ''.join(char for _, char in ngram_pairs))
        if ngram != last_ngram:
            yield ngram
        last_ngram = ngram


  '''
  generate all ngrams and then hash the string
  '''
  def ngrams_hashes(self, string, ngram_length):
    for line_number, ngram in self.ngrams(string, ngram_length):
      yield line_number, hash_function(ngram)


  '''
  go through every window of length n and choose the minimum
  n-gram hash within that window
  '''
  def window_hashes(self, string, ngram_length=NGRAM_LENGTH):
    ngram_iterator = self.ngrams(string, ngram_length)
    ngram_window = deque()
    previous = None
    try:
        for i in xrange(ngram_length):
          ngram_window.append(ngram_iterator.next())
        # do initial window
        yield min(reversed(ngram_window), key=lambda x: x[1])

        while True:
          ngram_window.popleft()
          ngram_window.append(ngram_iterator.next())
          # we always choose the right most minimum
          best = min(reversed(ngram_window), key=lambda x: x[1])
          # don't return the same as the previous one
          if best != previous:
              yield best
          previous = best
    except StopIteration:
        pass

  def group(self, matches):
      print matches
      raise Exception()
