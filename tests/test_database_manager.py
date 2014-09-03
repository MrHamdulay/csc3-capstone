import os
import sys
import unittest
sys.path.append(os.path.dirname(os.path.realpath(__file__))+'/../cheaters')
from database import DatabaseManager

''' Extend DatabaseManager with functionality to empty the tables
to test on an empty database'''
class DatabaseManager(DatabaseManager):

    def empty_tables(self):
        c = self.conn.cursor()
        c.execute('DELETE * FROM Matches')
        c.execute('DELETE * FROM Students')
        c.execute('DELETE * FROM Signatures')
        c.execute('DELETE * FROM Assignments')
        c.execute('DELETE * FROM Submissions')
        c.commit()


''' Database Manager Test Suite '''
class DatabaseManagerTests(unittest.TestCase):

    db_file = os.getcwd() + '/test.db'
    db = DatabaseManager(db_file)

    def empty_tables(self):
        '''Start with an empty database'''
        self.db.empty_tables()

    def test_student_table(self):
        course_code = 'CRS1000F'
        student_number = 'TSTSDN001'

        # insert, fetch
        self.db.insert_student(student_number, course_code)
        student = self.db.fetch_student(student_number, course_code)
        self.failUnless(student.student_number == student_number and student.course_code == course_code)

        # delete
        self.db.delete_student(student_number, course_code)
        student = self.db.fetch_student(student_number, course_code)
        self.failUnless(student == None)


if __name__ == '__main__':
    unittest.main()
