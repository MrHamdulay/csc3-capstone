import os
import zipfile
from StringIO import StringIO
from cheaters.detector import Detector

class DataGenerator:

    course_code = 'csc10015f'
    path = 'data'

    def get_assignment_number(name):
        ''' get the number out of an assignment
            folder string, such as Assignment_1
            @param String name, e.g. Assignment_1
            @return Int 1 '''
        return int(name.split('_')[1])

    def get_folder_names(path):
        ''' get the list of folder names in a directory
            @param String path
            @return Array'''
        os.chdir(path)
        folders = []
        for name in os.listdir('.'):
            if os.path.isdir(name):
                folders.append(name)
        return folders

    def get_file_names(path):
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
        folders = self.get_folder_names(self.path)
        for folder in folders:
            assignment_number = self.get_assignment_number(folder)
            # TODO
            # assignment = new Assignment(number, self.course_code)
            # db.insert_assignment(assignment)
            student_numbers = self.get_folder_names(folder)
            for student_number in student_numbers:
                # TODO
                # student = new Student(student_number)
                # db.insert_student(student, assignment)
                output_file = StringIO()
                zip = zipfile.ZipFile(output_file, 'w')
                for file in self.get_file_names(folder):
                    zip.write(os.path.join(folder, file), file)
                zip.close()
                detector = Detector()
                detector.run(output_file, assignment_number)
