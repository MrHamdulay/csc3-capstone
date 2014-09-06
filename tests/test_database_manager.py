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

# Hey Merishka =)

# The stuff for testing the database manager is below,
# the thing above is just to override it so that we have
# a method to empty the test database, which would be dangerous
# to have in the real manager.

# Small note on method names for the database manager:
#     It would be easier standardising the database methods
#     to CRUD related method names. So for example:
#        db.store_student vs db.data_populate
#        db.fetch_signatures vs db.lookup_my_signatures
#        db.fetch_assignments vs db.fetch_current_assignments
#        db.fetch_assignment (singular form of the above)
#        db.fetch_submission vs db.fetch_a_submission

# We also need delete methods for the tables,
# As these will be needed for cleaning up, and administration, so:
#       db.delete_student
#       db.delete_assignment
#       db.delete_submission
#       db.delete_matches
#       db.delete_signatures

# So we'll need those added in please.
# There's a test case for the student table below, as an example.
# It inserts something, finds it, deletes it, then tries to find it again.
# If it stumbles on any of the steps then it should fail. i.e. if it finds it
# after having deleted it.

# Thanks

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
        # db.store_assignment
        # db.fetch_current_assignments

    def test_submission_table(self):
        # db.store_submission
        # db.fetch_a_submission
        # db.fetch_submissions

    def test_signatures_table:
        # db.store_signatures method
        # db.lookup_my_signatures
        # db.lookup_matching_signatures (may be a little bit more complicated)

    def test_match_table:
        # db.store_matches
        # db.fetch_matches




if __name__ == '__main__':
    unittest.main()
