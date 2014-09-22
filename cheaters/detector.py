'''
Author: Yaseen Hamdulay, Jarred de Beer, Merishka Lalla
Date: 15 August 2014

Class that wraps the entire assignment submission process
excluding getting the file from the client to the server.
Including unzipping the file, detecting programming language,
concatenating all the files together, generating signatures
and storing results
'''
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
        Handles the submission process from the student/submit form

        detects language, generates signatures and stores results

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
            # this now happens in the background process
            #self.store_and_update_closest_matches(submission_id)
            print(str(assignment_number) + " " + student_number + " Saved")
        except SyntaxError:
            print(str(assignment_number) + " " + student_number + " Failed")
            pass

    def set_language_handler(self, zip_file):
        '''
        figures out language and loads the appropriate language handler

        @param submission list of files'''
        for filename in zip_file.namelist():
            extension = filename.split('.')[-1]
            if extension in Detector.LANGUAGES:
                self.language_handler = Detector.LANGUAGES[extension]()
                return extension
        raise UnknownLanguageException()

    def concatenate_files(self, zip_file):
        '''
        filters unneeded files and concatenates the program source together

        @param zip_file the zip of the submission
        @return string of the file put together
        '''
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
    def canonicalise_submission(submission):
        '''
        given a submission remove all variable names etc from it

        @return string program source with no identifying attributes
        '''
        language_handler = Detector.LANGUAGES[submission.language]()
        language_handler.parse_file(submission.program_source)
        return language_handler.strip_unstable_atrributes().replace(' ', '')
