import re
import zipfile


languages = ['py', 'java']
class Detector:
    ''' Encapsulates the entire parsing, signature generation and detection process '''

    def submit(self, files, assignment):
        '''
        @param files ZipFile object that contains students files
        @param assignment id of assignment submitting to
        '''
        assert isinstance(files,
        language = self.detect_language(files)
        submission = self.concatenate_files(files)
        algorithm

    def strip_unnecessary_files(self, files):
        '''
        @param submission list of files'''
        pass


    def detect_language(self, files):
        '''
        @param submission list of files'''

