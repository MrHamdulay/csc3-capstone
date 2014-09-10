import zipfile

from languages.python import PythonLanguageHandler
from languages.java import JavaLanguageHandler
from database.database import DatabaseManager
from algorithms.winnoweralgorithm import WinnowerAlgorithm
from algorithms.grouper import Grouper
from algorithms.suffix_tree import SuffixTree

class UnknownLanguageException(Exception):
    pass


class Detector:
    ''' Encapsulates the entire parsing, signature generation and detection process '''
    LANGUAGES = {
        'py': PythonLanguageHandler,
        'java': JavaLanguageHandler
    }

    matches = None
    signatures = None
    language_handler = None


    def run(self, submission, assignment_number, student_number):
        '''
        @param submission, File posted through web form
        @param assignment_number, Number of assignment
        '''
        zip_file = zipfile.ZipFile(submission)
        language = self.set_language_handler(zip_file)
        concatenated_file = self.concatenate_files(zip_file)

        self.language_handler.parse_file(concatenated_file)

        database = DatabaseManager()
        cheating_algorithm = WinnowerAlgorithm(self.language_handler)
        signatures = cheating_algorithm.generate_signatures()
        submission_id = database.store_submission(concatenated_file, assignment_number, student_number, language)
        database.store_signatures(signatures, submission_id)


    def set_language_handler(self, zip_file):
        '''
        @param submission list of files'''
        for filename in zip_file.namelist():
            extension = filename.split('.')[-1]
            if extension in Detector.LANGUAGES:
                self.language_handler = Detector.LANGUAGES[extension]()
                return extension
        raise UnknownLanguageException()

    def delete_assignment(self,assignmentNumber):
        db = DatabaseManager()
        db.delete_assignment(assignmentNumber)
        print('Assignment deleted')

    def concatenate_files(self, zip_file):
        concatenated_file = ''
        for filename in zip_file.namelist():
            if '__MACOSX' in filename:
                continue
            extension = filename.split('.')[-1]
            print filename, extension, extension in self.language_handler.file_types
            if extension in self.language_handler.file_types:
                concatenated_file += zip_file.read(filename)
        return concatenated_file

    def runAssignment(self,description, dueDate,courseCode):
        database = DatabaseManager()
        database.store_assignment(courseCode, description,dueDate)
        print('stored')

    @staticmethod
    def find_most_similar_submission(submission):
        database = DatabaseManager()
        grouper = Grouper()

        # TODO: this can probably be done in one sql query without post processing
        signatures = database.lookup_matching_signatures(submission.id)
        grouped_signatures = grouper.group_signatures_by_document(signatures)

        while True:
            closest_submission_id = max(grouped_signatures.iteritems(), key=lambda x: len(x[1]))[0]
            other_submission = database.fetch_a_submission(submission.assignment_id,
                    closest_submission_id)
            # it only makes sense to compare the same language
            if other_submission.language != submission.language:
                del grouped_signatures[closest_submission_id]
            else:
                return other_submission
        return None

    @staticmethod
    def canonicalise_submission(submission):
        language_handler = Detector.LANGUAGES[submission.language]()
        language_handler.parse_file(submission.program_source)
        return language_handler.strip_unstable_atrributes()

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
            string_indexes = Detector.remove_overlapping_ranges(temp)

            line_numbers = Detector.string_indexes_to_line_numbers(canonicalised[i], string_indexes)

            document_matches.append(line_numbers)

        raise Exception
