import os
import sys
import unittest
sys.path.append(os.path.dirname(os.path.realpath(__file__))+'/../cheaters')
from database import DatabaseManager


''' Extend DatabaseManager with functionality to empty the tables
so we can test on an empty database'''
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
        self.db.store_student(student_number, course_code)
        student = self.db.fetch_student(student_number, course_code)
        self.failUnless(student.student_number == student_number and student.course_code == course_code)

        # delete
        self.db.delete_student(student_number, course_code)
        student = self.db.fetch_student(student_number, course_code)
        self.failUnless(student == None)

    def test_assignment_table(self):
        course_code = 'CRS1000F'
        description = 'assignment 1 for the course'
        due = '9/2/2014'
        self.db.store_assignment(course_code,description,due)
        assignment = self.db.fetch_current.assignments()
        self.failUnless(assignment == None)


    def test_submission_table(self):
        # self.db.store_submission()
        subId = 1
        assignmentId = 1
        submission = self.db.fetch_a_submission(subId, assignmentId)
        self.failUnless(submission == None)
        submissions = self.db.fetch_a_submissions(assignmentId)
        self.failUnless(submissions == None)

    def test_signatures_table(self):
        # db.store_signatures()
        submissionId = 1
        signatures = self.db.lookup_my_signatures(submissionId)
        self.failUnless(signatures== None)

        signatureList = self.db.lookup_matching_signatures (submissionId)
        self.failUnless(signatureList == None)

    def test_match_table(self):
        #db.store_matches

        matches =self.db.fetch_matches()
        self.failUnless(matches == None)



if __name__ == '__main__':
    unittest.main()
