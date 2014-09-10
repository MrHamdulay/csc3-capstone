from detector import Detector
from algorithms.suffix_tree import SuffixTree

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

        result = []
        for begin, end in indexes:
            result.append((string_line_numbers[begin], string_line_numbers[end]))
        return result


    @staticmethod
    def calculate_document_similarity(submission1, submission2):
        assert submission1.language == submission2.language
        canonicalised = [
                Detector.canonicalise_submission(submission1),
                Detector.canonicalise_submission(submission2)]

        st = SuffixTree(canonicalised)
        common_substrings = list(st.common_substrings_longer_than(20))
        # longest to shortest
        common_substrings.sort(key=lambda x: len(x), reverse=True)

        document_matches = []

        # find the indexes of the strings and remove all overlapping occurrences
        for i in xrange(2):
            temp = []
            for substring in common_substrings:
                index = canonicalised[i].index(substring)
                temp.append((index, index + len(substring)))
            string_indexes = SuffixTreeAlgorithm.remove_overlapping_ranges(temp)

            line_numbers = SuffixTreeAlgorithm.string_indexes_to_line_numbers(canonicalised[i], string_indexes)

            document_matches.append(line_numbers)

        raise Exception
