import os
import sys
import unittest
import os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'cheaters'))

from database import DatabaseManager
from model.signature import Signature


''' Extend DatabaseManager with functionality to empty the tables
so we can test on an empty database'''
class DatabaseManager(DatabaseManager):

    def empty_tables(self):
        c = self.conn.cursor()
        c.execute('DELETE FROM Students')
        c.execute('DELETE FROM Signatures')
        c.execute('DELETE FROM Assignments')
        c.execute('DELETE FROM Submissions')
        c.close()
        self.conn.commit()

''' Database Manager Test Suite '''
class DatabaseManagerTests(unittest.TestCase):

    db_file = os.path.join(os.getcwd(), 'test.db')
    db = DatabaseManager(db_file)

    def __init__(self, *args):
        self.empty_tables()
        unittest.TestCase.__init__(self, *args)

    def empty_tables(self):
        '''Start with an empty database'''
        self.db.empty_tables()


    def test_student_table(self):
        course_code = 'CRS1000F'
        student_number = 'TSTSDN002'

        # insert, fetch
        self.db.data_populate(student_number, course_code)
        student = self.db.fetch_student(student_number)
        print(student)


        # delete
        self.db.delete_student(student_number)


    def test_assignment_table(self):
        course_code = 'CRS1000F'
        description = 'assignment 1 for the course'
        due = '9/2/2014'
        assignment = []
        self.db.store_assignment(course_code, description, due)

        assignment = self.db.fetch_current_assignments()
        self.failUnless(assignment.course_code == course_code )
        print(assignment)
        self.failUnless(assignment)


    def test_submission_table(self):

        c_file = "print (hello world) print(tomorrow this assignment is over =D ) eurhwrfhireheifibivbsdkbkvbhbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
        subId = 1
        assignmentId = 1
        languagefile = "python"

        self.db.store_submission(c_file, subId, assignmentId,languagefile)

        submission = self.db.fetch_a_submission(subId, assignmentId)
        print(submission)
        self.failUnless(submission)
        submissions = self.db.fetch_submissions(assignmentId)
        print(submissions)


    def test_signatures_table(self):

        self.db.store_signatures([Signature('(i)whii:',100,3), Signature('(i)whii:',100,3)],100)
        self.db.store_signatures([Signature('(i)whii:',101,3), Signature('(i)whii:',101,3)],101)
        signatures = self.db.lookup_matching_signatures(100)
        print(signatures)
        self.assertEqual(str(signatures[0]),'[<Submission id:1 student_number:1 source_len:139 assignment_id:1 submission_date:2014-09-21>')


if __name__ == '__main__':
    unittest.main()
