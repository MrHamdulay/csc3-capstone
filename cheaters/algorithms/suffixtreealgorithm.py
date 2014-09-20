from detector import Detector
from algorithms.suffix_tree import SuffixTree
from model.match import Match

class SuffixTreeAlgorithm:

    @staticmethod
    def remove_overlapping_ranges(ranges):
        ranges.sort()

        result = [ranges[0]]

        for i in xrange(1, len(ranges)):
            if result[-1][0] <= ranges[i][0] <= result[-1][1]:
                old_range = result.pop()
                result.append((old_range[0], max(ranges[i][1], old_range[1])))
            else:
                result.append(ranges[i])
        return result

    @staticmethod
    def string_indexes_to_line_numbers(string, indexes):
        # pre process string
        string_line_numbers = []
        n=0
        for c in string:
            if c == '\n':
                n += 1
            string_line_numbers.append(n)
        string_line_numbers.append(n)

        result = []
        for begin, end in indexes:
            result.append((string_line_numbers[begin], string_line_numbers[end]))
        return result


    @staticmethod
    def filter_substrings(substring):
        lines = [x.strip() for x in substring.split('\n')]
        lines = filter(None, lines)
        return len(lines)>3

    @staticmethod
    def _wrap_to_lines(code, index, direction):
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


    @staticmethod
    def wrap_substring_to_lines(code, begin, end):
        return (SuffixTreeAlgorithm._wrap_to_lines(code, begin, +1),
               SuffixTreeAlgorithm._wrap_to_lines(code, end, -1))


    @staticmethod
    def calculate_document_similarity(*submissions):
        assert len(submissions) == 2
        assert submissions[0].language == submissions[1].language
        canonicalised = map(Detector.canonicalise_submission, submissions)

        st = SuffixTree(canonicalised)
        common_substrings = list(st.common_substrings_longer_than(20))
        common_substrings = filter(SuffixTreeAlgorithm.filter_substrings, common_substrings)
        # longest to shortest
        common_substrings.sort(key=lambda x: len(x), reverse=True)

        document_matches = []

        # find the indexes of the strings and remove all overlapping occurrences
        for i in xrange(2):
            string_indexes = []
            for substring in common_substrings:
                index = canonicalised[i].index(substring)
                string_indexes.append(SuffixTreeAlgorithm.wrap_substring_to_lines(canonicalised[i], index, index + len(substring)))

            temp = SuffixTreeAlgorithm.string_indexes_to_line_numbers(canonicalised[i], string_indexes)
            line_numbers = SuffixTreeAlgorithm.remove_overlapping_ranges(temp)

            matches = []
            for begin, end in line_numbers:
                matches.append(Match(submissions[i].id, begin, end - begin, 0))


            document_matches.append(matches)

        return document_matches
