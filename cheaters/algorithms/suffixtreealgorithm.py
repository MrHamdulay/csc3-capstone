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
        return len(lines)>2

    @staticmethod
    def calculate_document_similarity(*submissions):
        assert len(submissions) == 2
        assert submissions[0].language == submissions[1].language
        canonicalised = map(Detector.canonicalise_submission, submissions)

        st = SuffixTree(canonicalised)
        common_substrings = list(st.common_substrings_longer_than(20))
        common_substrings = filter(SuffixTreeAlgorithm.filter_substrings, common_substrings)
        print 'common substrings'
        print '\n'.join('START\n%s\n END'%x for x in  common_substrings)
        # longest to shortest
        common_substrings.sort(key=lambda x: len(x), reverse=True)

        document_matches = []

        # find the indexes of the strings and remove all overlapping occurrences
        for i in xrange(2):
            string_indexes = []
            for substring in common_substrings:
                index = canonicalised[i].index(substring)
                string_indexes.append((index, index + len(substring)))
            print 'string indexes', string_indexes

            temp = SuffixTreeAlgorithm.string_indexes_to_line_numbers(canonicalised[i], string_indexes)
            line_numbers = SuffixTreeAlgorithm.remove_overlapping_ranges(temp)
            print 'line numbers', line_numbers

            matches = []
            for begin, end in line_numbers:
                matches.append(Match(submissions[i].id, begin, end - begin, 0))


            document_matches.append(matches)

        return document_matches
