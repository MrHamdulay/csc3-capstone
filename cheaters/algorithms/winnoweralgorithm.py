from algorithms.base import BaseAlgorithm, SectionMatch
from collections import deque, defaultdict

WINDOW_LENGTH = 11
NGRAM_LENGTH = 5


'''
algorithm that implements the winnower search method described
in the MOSS whitepaper
'''
class WinnowerAlgorithm(BaseAlgorithm):
  ALLOWED_LANGUAGE_EXTENSIONS = ['*']
  MINIMUM_SIGNATURES_MATCH_THRESHOLD = 5

  def __init__(self):
    self.current_ngrams = defaultdict(list)

  def isPlagiarised(self, program):
    canonicalised_ = program.canonicalised_program_source

    # generate, store and look up all winnower hashes
    program_matches = defaultdict(list)
    for line_number, h in self.window_hashes(program.canonicalised_program_source):
      if h in self.current_ngrams:

        for program_match, match_line_number in self.current_ngrams[h]:
          if program_match != program:
              program_matches[program_match].append((line_number, match_line_number))
      self.current_ngrams[h].append((program, line_number))

    # filter out programs that matched below the threshold
    for other_program, matches in program_matches.iteritems():
        if len(matches) < self.MINIMUM_SIGNATURES_MATCH_THRESHOLD:
            del program_matches[other_program]

    for other_program, matches in program_matches.iteritems():
        # needs to be consecutive matches within a program match
        for original_line, matched_line in matches:
            match = SectionMatch(program, original_line, original_line+1)
            program.mark_cheated(match)
            other_program.mark_cheated(SectionMatch(other_program, matched_line, matched_line+1))


  '''
  given a string and a length generate and return all
  length-grams of this string'''
  def ngrams(self, string, ngram_length):
    line_number = 0
    string = string.replace(' ', '')
    for i in xrange(len(string)-ngram_length+1):
      if string[i] == '\n':
        line_number += 1
      ngram = string[i:i+ngram_length]
      # skip blank ngrams
      if len(ngram.strip()):
          yield (line_number, ngram)


  '''
  generate all ngrams and then hash the string
  '''
  def ngrams_hashes(self, string, ngram_length):
    for line_number, ngram in self.ngrams(string, ngram_length):
      yield line_number, hash(ngram)


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
