from detector import Detector
from algorithms.suffix_tree import SuffixTree
from model.match import Match
from external.no_indent_tokenize import generate_tokens
from StringIO import StringIO

class SuffixTreeAlgorithm:
    def _variable_match(self, *originals):
        tokenlists = []
        for original in originals:
            tokenlists.append(list(x[1] for x in generate_tokens(StringIO(original).readline) if x[0] == 1))

        token_map = {}
        for token1, token2 in zip(*tokenlists):
            if token1 in token_map and token_map[token1] != token2:
                return False
            token_map[token1] = token2
        return True

    def remove_overlapping_ranges(self, ranges):
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


    def filter_substrings(self, substring):
        lines = [x.strip() for x in substring.split('\n')]
        lines = filter(None, lines)
        return len(lines)>3

    def _wrap_to_lines(self, code, index, direction):
        # check for non whitespace characters before this
        i = index - direction
        isInMiddleLine = False
        while i >= 0 and i < len(code):
            if code[i] == '\n':
                break
            if code[i] not in '\t ':
                isInMiddleLine = True
                break
            i -= direction
        if isInMiddleLine:
            # find first newline in direction
            i = index
            while i>=0 and i<len(code) and code[i] != '\n':
                i += direction
            return i
        else:
            return index


    def wrap_substring_to_lines(self, code, begin, end):
        return (self._wrap_to_lines(code, begin, +1),
               self._wrap_to_lines(code, end, -1))


    def calculate_document_similarity(self, *submissions):
        assert len(submissions) == 2
        assert submissions[0].language == submissions[1].language
        canonicalised = map(Detector.canonicalise_submission, submissions)

        st = SuffixTree(canonicalised)
        common_substrings = list(st.common_substrings_longer_than(20))
        common_substrings = filter(self.filter_substrings, common_substrings)
        # longest to shortest
        common_substrings.sort(key=lambda x: len(x), reverse=True)

        document_matches = [[], []]
        string_indexes = [[], []]
        to_line_number = map(self.string_indexes_to_line_numbers, canonicalised)
        to_line_number[0].send(None)
        to_line_number[1].send(None)

        source_lines = map(lambda x: x.program_source.split('\n'), submissions)

        for substring in common_substrings:
            indexes = []
            substring_originals = []
            for i in (0, 1):
                index = canonicalised[i].index(substring)
                wrapped_index = self.wrap_substring_to_lines(canonicalised[i], index, index + len(substring))
                line_index = to_line_number[i].send(wrapped_index)
                indexes.append(line_index)
                substring_originals.append('\n'.join(source_lines[i][line_index[0]:line_index[1]]))

            # only add this index if we can match variables
            if self._variable_match(*substring_originals):
                for i in (0, 1):
                    string_indexes[i].append(indexes[i])

        for i in (0, 1):
            line_numbers = self.remove_overlapping_ranges(string_indexes[i])

            for begin, end in line_numbers:
                document_matches[i].append(Match(submissions[i].id, begin, end - begin, 0))

        return document_matches
