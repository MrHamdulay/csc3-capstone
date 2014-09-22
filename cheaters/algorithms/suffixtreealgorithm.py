'''
Author: Yaseen Hamdulay, Jarred de Beer, Merishka Lalla
Date: 15 August 2014

Using suffix trees to find similarity between pairs of documents
'''
from detector import Detector
from algorithms.suffix_tree import SuffixTree
from model.match import Match
from external.no_indent_tokenize import generate_tokens
from StringIO import StringIO

class SuffixTreeAlgorithm:
    def _variable_match(self, *originals):
        ''' given two strings of code find a bijection between the identifiers if one exists.
        @param originals strings of program source code
        @returns boolean whether there is a bijection between class names and variable names'''
        tokenlists = []
        for original in originals:
            tokenlists.append(list(x[1] for x in generate_tokens(StringIO(original).readline) if x[0] == 1))

        token_map = {}
        for token1, token2 in zip(*tokenlists):
            if token1 in token_map and token_map[token1] != token2:
                return False
            token_map[token1] = token2
        return True

    def _remove_overlapping_ranges(self, ranges):
        '''
        Given a list of ranges, merge all overlapping ranges

        @param ranges list of tuples
        @returns list of tuples with overlapping ranges merged'''
        if not ranges:
            return []
        ranges.sort()

        result = [ranges[0]]

        for i in xrange(1, len(ranges)):
            if result[-1][0] <= ranges[i][0] <= result[-1][1]:
                old_range = result.pop()
                result.append((old_range[0], max(ranges[i][1], old_range[1])))
            else:
                result.append(ranges[i])
        return result

    def string_indexes_to_line_numbers(self, string):
        '''
        return a generator for a string that given an index into the
        string return the line number the index is on

        @param string string to be indexed
        @returns generator that generates line numbers (see coroutines)'''
        # pre process string
        string_line_numbers = []
        n=0
        for c in string:
            if c == '\n':
                n += 1
            string_line_numbers.append(n)
        string_line_numbers.append(n)

        begin, end = yield

        while True:
            begin, end = yield (string_line_numbers[begin], string_line_numbers[end])


    def _wrap_to_lines(self, lines, code, index, direction):
        ''' private method that moves an index to the end/beginning of the current line'''
        code = code+'\n'
        if index > 0 and index < len(code):
            if lines[index] == lines[index-direction]:
                # find first newline in direction
                i = index
                while i>=0 and i<len(code) and lines[i] == lines[i-direction]:
                    i += direction
                return i
        return index


    def _wrap_substring_to_lines(self, code, lines, begin, end):
        '''
        given a range in the source code shrink indexes to middle new lines
        if we cover a partial line or leave it the same if we are on the edges of the line '''
        our_lines = lines+[lines[-1]+1]
        return (self._wrap_to_lines(our_lines, code, begin, +1),
                self._wrap_to_lines(our_lines, code, end, -1))

    def _whitespaced_stripped_with_line_numbers(self, string):
        '''
        strips whitespace and new lines and generates a list of line numbers
        so we can re-add line information when necessary

        @param string program source input
        @returns [stripped string, line numbers]
        '''
        WHITESPACE = ' \n\t'
        line_number = 0
        s = ''
        line_numbers = []
        for char in string:
            if char == '\n':
                line_number += 1
            if char in WHITESPACE:
                continue
            s += char
            line_numbers.append(line_number)
        line_numbers.append(line_number)
        return s, line_numbers

    def calculate_document_similarity(self, *submissions):
        '''
        given a list of submissions find source code matches between them
        '''
        assert len(submissions) == 2
        assert submissions[0].language == submissions[1].language
        line_numbers = []
        canonicalised = []
        # strip whitespace, new lines and remove variable names etc
        for submission in submissions:
            document = Detector.canonicalise_submission(submission)
            s, l = self._whitespaced_stripped_with_line_numbers(document)
            line_numbers.append(l)
            canonicalised.append(s)

        # generate generalised suffix tree
        st = SuffixTree(canonicalised)
        # find long common substrings
        common_substrings = list(st.common_substrings_longer_than(20))
        # longest to shortest
        common_substrings.sort(key=lambda x: len(x), reverse=True)

        document_matches = [[], []]
        string_indexes = [[], []]

        source_lines = map(lambda x: x.program_source.split('\n'), submissions)

        # match substrings back into line numbers
        for substring in common_substrings:
            startAt = [0, 0]
            # the substrings may occur multiple times in the string so loop until we can no longer find them
            while True:
                indexes = []
                substring_originals = []
                empty = False
                newStartAt = startAt[:]
                for i in (0, 1):
                    index = canonicalised[i].find(substring, startAt[i])
                    # we may find this again next time
                    if index != -1:
                        newStartAt[i] = index+1
                    else:
                        # we couldn't find it again, just use the old index
                        index = canonicalised[i].find(substring)
                    index = self._wrap_substring_to_lines(canonicalised[i], line_numbers[i], index, index + len(substring))
                    # it wrapped to 0 lines so we ignore it
                    if index[0] >= index[1]:
                        empty = True
                        continue
                    line_index = line_numbers[i][index[0]], line_numbers[i][index[1]]
                    indexes.append(line_index)
                    substring_originals.append('\n'.join(source_lines[i][line_index[0]:line_index[1]]))

                if startAt == newStartAt:
                    break
                startAt = newStartAt

                # only add this index if we can match variables
                if not empty and self._variable_match(*substring_originals):
                    for i in (0, 1):
                        string_indexes[i].append(indexes[i])

        for i in (0, 1):
            line_numbers = self._remove_overlapping_ranges(string_indexes[i])

            for begin, end in line_numbers:
                if end - begin > 1:
                    document_matches[i].append(Match(submissions[i].id, begin, end - begin, 0))

        return document_matches
