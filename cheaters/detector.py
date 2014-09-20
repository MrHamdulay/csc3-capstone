import zipfile

from languages.python import PythonLanguageHandler
from languages.java import JavaLanguageHandler
from database.database import DatabaseManager
from algorithms.winnoweralgorithm import WinnowerAlgorithm
from algorithms.grouper import Grouper

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
        try:
            self.language_handler.parse_file(concatenated_file)

            database = DatabaseManager()
            cheating_algorithm = WinnowerAlgorithm(self.language_handler)
            signatures = cheating_algorithm.generate_signatures()
            submission_id = database.store_submission(concatenated_file, assignment_number, student_number, language)
            database.store_signatures(signatures, submission_id)
            #self.store_and_update_closest_matches(submission_id)
            print(str(assignment_number) + " " + student_number + " Saved")
        except SyntaxError:
            print(str(assignment_number) + " " + student_number + " Failed")
            pass

    def store_and_update_closest_matches(self, submission_id):
        database = DatabaseManager()
        grouper = Grouper()
        matching_signatures = database.lookup_matching_signatures(submission_id)
        signatures_by_document = grouper.group_signatures_by_document(matching_signatures)

        if not signatures_by_document:
            return
        other_submission_id = max(signatures_by_document.iteritems(), key=lambda x: len(x[1]))[0]
        database.store_submission_match(submission_id, other_submission_id, len(signatures_by_document[other_submission_id]))

        for other_submission_id, signatures in signatures_by_document.iteritems():
            num_signatures = len(signatures)
            signature_match = database.fetch_submission_match(other_submission_id)

            if signature_match is None:
                continue
            if num_signatures > signature_match.number_signatures_matched:
                database.update_submission_match(
                        signature_match,
                        match_submission_id=other_submission_id,
                        number_signatures_matched=num_signatures)


    def set_language_handler(self, zip_file):
        '''
        @param submission list of files'''
        for filename in zip_file.namelist():
            extension = filename.split('.')[-1]
            if extension in Detector.LANGUAGES:
                self.language_handler = Detector.LANGUAGES[extension]()
                return extension
        raise UnknownLanguageException()

    def concatenate_files(self, zip_file):
        concatenated_file = ''
        for filename in zip_file.namelist():
            if '__MACOSX' in filename:
                continue
            extension = filename.split('.')[-1]
            print filename, extension, extension in self.language_handler.file_types
            if extension in self.language_handler.file_types:
                concatenated_file += zip_file.read(filename) + '\n'
        return concatenated_file

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
