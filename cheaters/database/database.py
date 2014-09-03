'''author = 'Merishka Lalla
A database class to manage all insertions into different tables. These tables being Students, Assignments, Signatures
and Matches. Each table has a series of different values but linked together through a Primary Key which is linked through
an ID and a foreign key which is linked through other relevant column values.

Database used was sqlite3.
'''

#__author__ = 'Merishka Lalla'
import os
import sqlite3
from model.signature import Signature
from model.assignment import Assignment
from model.submissions import Submission

class DatabaseManager:
    conn = None

    '''A initiator method to allow the database to connect to the class for further database handling.'''
    def __init__(self, database_file='cheaters.db'):
        self.conn = sqlite3.connect(database_file)
        '''The initialise database method connects a cursor and reads a sql script. The script is read and executed.
        Once executed, tables with relevant columns is created and initiated. There after the cursor is closed and the
        changes are committed.'''
        self.initialise_database()

    def initialise_database(self):
        c = self.conn.cursor()
        file = open(os.path.dirname(os.path.realpath(__file__))+'/schema.sql','r')
        c.executescript(file.read())
        c.close()
        self.conn.commit()
    '''Store_signatures stores the signatures which have been generated. These signatures show the aspects of code which
      are suspected to be copied or cheated. The generated signatures are stored in the database using the insert method.
      Signatures is a list and is stored element by element before cursor is closed.'''

    def store_signatures(self,signatures,submission_id):
        c = self.conn.cursor()
        for s in signatures:
            signature_values = (s.line_number_mine,s.ngram_hash, submission_id)
            c.execute("INSERT INTO Signatures(LineNumber,NgramHash,SubmissionId) VALUES(?,?,?)",signature_values)
        c.close()
        self.conn.commit()
    '''store_submissions stores the submissions sent to the program which is used to be checked against other submissions. '''
    def store_submission(self,concatenated_file, assignment_number, student_number):
        c = self.conn.cursor()
        submission_value = (student_number, assignment_number, concatenated_file)

        c.execute("INSERT INTO Submissions (StudentId,AssignmentNumber, ProgramSource) VALUES (?,?,?)",submission_value)
        submission_id = c.lastrowid
        c.close()
        self.conn.commit()
        return submission_id

    def store_matches(self,grouped_matches, submission_id):
        c = self.conn.cursor()
        for document_submission_id, document_matches in grouped_matches.iteritems():
            for match in document_matches:
                c.execute('INSERT INTO Matches (SubmissionIdMine, SubmissionIdTheirs, StartLineMine,'
                    ', StartLineTheirs, LengthOfMatch) VALUES (?, ?, ?, ?)',
                    (submission_id, match.submission_id, match.start_line_mine, match.start_line_theirs,
                     match.match_length))

        c.close()
        self.conn.commit()

    def lookup_my_signatures(self, submission_id):
        c = self.conn.cursor()
        c.execute('SELECT LineNumber, NgramHash FROM Signatures WHERE SubmissionId = ?', (submission_id,))
        signatures = [Signature(x[1], submission_id, x[0]) for x in c]
        c.close()
        return signatures


    '''Lookup_signatures looks up signatures which will be used to check for potential cheating or copied code. '''
    def lookup_matching_signatures(self, submission_id):
        c = self.conn.cursor()
        c.execute('SELECT s1.SubmissionId, s1.LineNumber, s2.LineNumber, s1.NgramHash, s2.SubmissionId FROM Signatures as s1 '
                'JOIN Signatures as s2 ON s1.NgramHash = s2.NgramHash WHERE s1.SubmissionId = ? AND s2.SubmissionId != s1.SubmissionId',
                (submission_id, ))
        signatures = [Signature(row[3], row[0], row[1], row[4], row[2])  for row in c]
        c.close()
        return signatures

    '''Data populate is a method used to insert students into the database for testing.'''
    def data_populate(self,student_number, course_code):
        c = self.conn.cursor()
        data_Values = (student_number,course_code)
        c.execute("INSERT INTO Students (StudentNumber, CourseCode) VALUES (?,?,?)",data_Values)
        c.close()
        self.conn.commit()

    def fetch_current_assignments(self):
        c = self.conn.cursor()
        c.execute('SELECT Id, CourseCode, AssignmentDescription FROM Assignments')# WHERE DueDate >= CURRENT_DATE')
        assignments = []
        for row in c:
            assignments.append(Assignment(*row))
        c.close()
        return assignments

    def fetch_a_submission(self, assignment_id, submission_id):
        c = self.conn.cursor()
        c.execute('SELECT Id, StudentId, AssignmentNumber, ProgramSource, SubmissionDate FROM Submissions WHERE AssignmentNumber = ? AND Id = ?' ,(assignment_id, submission_id))
        submission = None
        for x in c:
            submission = Submission(
                    id=x[0],
                    student_number=x[1],
                    program_source=x[3],
                    assignment_id=x[2],
                    submission_date=x[4])
        c.close()
        return submission


    def fetch_submissions(self, assignment_id):
        c = self.conn.cursor()
        submissions = []
        c.execute('SELECT Id, StudentId, AssignmentNumber, ProgramSource, SubmissionDate FROM Submissions WHERE AssignmentNumber = ?' ,(assignment_id, ))
        for x in c:
            submissions.append(
                Submission(
                    id=x[0],
                    student_number=x[1],
                    program_source=x[3],
                    assignment_id=x[2],
                    submission_date=x[4]))
        c.close()
        return submissions

    def fetch_matches(self, submission_id):
        c = self.conn.cursor()
        c.execute('SELECT MatchSubmissionId, LinesMatched, LengthOfMatch')
    #I've taken out student_number as a variable passed to the method as the lecturer will specify courseCode. It's only
    #when students submit an assignment then student_number will be necessary.
    def store_assignment(self, assignment_description,due_date,courseCode):
        c = self.conn.cursor()

       # courseCode = c.execute('SELECT CourseCode FROM Students where StudentNumber = ?', (student_number, ))

        assignmentValues = (assignment_description,due_date,courseCode)

        c.execute('INSERT INTO Assignments (AssignmentDescription,DueDate,CourseCode) VALUES (?,?,?)',assignmentValues)
        c.close()
        self.conn.commit()

