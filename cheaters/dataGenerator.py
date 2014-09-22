'''
Author: Yaseen Hamdulay, Jarred de Beer, Merishka Lalla
Date: 15 August 2014

Script to read in data given to us by Hussein into our database
'''
import os
import zipfile
from StringIO import StringIO
from detector import Detector
from database.database import DatabaseManager

class DataGenerator:

    course_code = 'csc10015f'
    path = os.path.join(os.getcwd(), '../examples/data')

    def get_assignment_number(self, name):
        ''' get the number out of an assignment
            folder string, such as Assignment_1
            @param String name, e.g. Assignment_1
            @return Int 1 '''
        return int(name.split('_')[1])

    def get_folder_names(self, path):
        ''' get the list of folder names in a directory
            @param String path
            @return Array'''
        os.chdir(path)
        folders = []
        for name in os.listdir('.'):
            if os.path.isdir(name):
                folders.append(name)
        return folders

    def get_file_names(self, path):
        ''' get the list of file names in a directory
            @param String path
            @return Array'''
        os.chdir(path)
        files = []
        for name in os.listdir('.'):
            if os.path.isfile(name):
                files.append(name)
        return files

    def run(self):
        '''Reads assignments from Assignment_* folders, student numbers from
           their Assignment_x folder, generates a zip of each students' code
           files and runs the Detector on it'''
        assignment_id_map = {}
        assignments = self.get_folder_names(self.path)
        database = DatabaseManager()
        for assignment in assignments:
            document_assignment_number = self.get_assignment_number(assignment)
            if document_assignment_number not in  (6, 7):
                continue
            if document_assignment_number not in assignment_id_map:
                name = 'Assignment %d' % document_assignment_number
                assignment_id_map[document_assignment_number] = database.store_assignment(name, name, '2015-01-01')
            assignment_number = assignment_id_map[document_assignment_number]
            assignment_path = os.path.join(self.path, assignment)
            student_numbers = self.get_folder_names(assignment_path)
            for student_number in student_numbers:
                student_folder = os.path.join(assignment_path, student_number)
                output_file = StringIO()
                zip = zipfile.ZipFile(output_file, 'w')
                for file in self.get_file_names(student_folder):
                    zip.write(os.path.join(student_folder, file), file)
                    print('zipping: ' + file)
                zip.close()
                detector = Detector()
                detector.run(output_file, assignment_number,student_number)

if __name__ == '__main__':
    g = DataGenerator()
    g.run()
