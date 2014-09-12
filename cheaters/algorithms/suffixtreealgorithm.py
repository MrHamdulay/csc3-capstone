from detector import Detector
from algorithms.suffix_tree import SuffixTree
from algorithms.winnoweralgorithm import WinnowerAlgorithm
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
    def calculate_document_similarity(*submissions):
        assert len(submissions) == 2
        assert submissions[0].language == submissions[1].language
        canonicalised = []
        canonicalised_line_numbers = []
        for s in submissions:
            # remove all whitespace
            stripped_string = WinnowerAlgorithm.whitespaced_stripped_with_line_numbers(
                    Detector.canonicalise_submission(s))
            lines = []
            string = []
            for line, c in stripped_string:
                lines.append(line)
                string.append(c)
            lines.append(line)
            canonicalised.append( ''.join(string))
            canonicalised_line_numbers.append(lines)

        st = SuffixTree(canonicalised)
        common_substrings = list(st.common_substrings_longer_than(20))
        # longest to shortest
        common_substrings.sort(key=lambda x: len(x), reverse=True)

        document_matches = []

        # find the indexes of the strings and remove all overlapping occurrences
        for i in xrange(2):
            indexes = []
            line_numbers = []
            for substring in common_substrings:
                index = canonicalised[i].index(substring)
                indexes.append((index, index+len(substring)))

            indexes = SuffixTreeAlgorithm.remove_overlapping_ranges(indexes)
            for index in indexes:
                line_numbers.append((canonicalised_line_numbers[i][index[0]], canonicalised_line_numbers[i][index[1]]))

            matches = []
            for begin, end in line_numbers:
                matches.append(Match(submissions[i].id, begin, end - begin, 0))


            document_matches.append(matches)

        return document_matches
