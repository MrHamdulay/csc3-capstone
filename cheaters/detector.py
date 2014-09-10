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
    def calculate_document_similarity(submission1, submission2):
        assert submission1.language == submission2.language
        submission1_canonicalised = Detector.canonicalise_submission(submission1)
        submission2_canonicalised = Detector.canonicalise_submission(submission2)

        st = SuffixTree([submission1_canonicalised, submission2_canonicalised])
        common_substrings = st.common_substrings_longer_than(10)
