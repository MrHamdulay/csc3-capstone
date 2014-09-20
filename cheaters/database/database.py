'''author = 'Merishka Lalla
A database class to manage all insertions into different tables. These tables being Students, Assignments, Signatures
and Matches. Each table has a series of different values but linked together through a Primary Key which is linked through
an ID and a foreign key which is linked through other relevant column values.

Database used was sqlite3.
'''

#__author__ = 'Merishka Lalla'
import os
import sqlite3
import time
from model.signature import Signature
from model.assignment import Assignment
from model.submissions import Submission
from model.signaturematch import SignatureMatch
from signaturemanager import SignatureManager

class DatabaseManager:
    conn = None

    '''A initiator method to allow the database to connect to the class for further database handling.'''
    def __init__(self, database_file='cheaters.db'):
        self.conn = sqlite3.connect(os.path.dirname(os.path.realpath(__file__))+'/../../'+database_file)
        self.conn.text_factory = str
        '''The initialise database method connects a cursor and reads a sql script. The script is read and executed.
        Once executed, tables with relevant columns is created and initiated. There after the cursor is closed and the
        changes are committed.'''
        self.initialise_database()
        self.initialise_signature_manager()

    def initialise_database(self):
        c = self.conn.cursor()
        file = open(os.path.dirname(os.path.realpath(__file__))+'/schema.sql','r')
        c.executescript(file.read())
        c.close()
        self.conn.commit()

    def initialise_signature_manager(self):
        self.signature_manager = SignatureManager()
        c = self.conn.cursor()
        c.execute('SELECT NgramHash, SubmissionId, LineNumber FROM Signatures')
        result = []
        for row in c:
            self.signature_manager.store_signature(Signature(*row), row[1])
        c.close()


    '''Store_signatures stores the signatures which have been generated. These signatures show the aspects of code which
      are suspected to be copied or cheated. The generated signatures are stored in the database using the insert method.
      Signatures is a list and is stored element by element before cursor is closed.'''

    def store_signatures(self,signatures,submission_id):
        c = self.conn.cursor()
        for s in signatures:
            signature_values = (s.line_number_mine,s.ngram_hash, submission_id)
            c.execute("INSERT INTO Signatures(LineNumber,NgramHash,SubmissionId) VALUES(?,?,?)",signature_values)
            self.signature_manager.store_signature(s, submission_id)
        c.close()
        self.conn.commit()

    '''store_submissions stores the submissions sent to the program which is used to be checked against other submissions. '''
    def store_submission(self,concatenated_file, assignment_number, student_number, langauge):
        c = self.conn.cursor()
        submission_value = (student_number, assignment_number, concatenated_file, langauge)

        c.execute("INSERT INTO Submissions (StudentId,AssignmentNumber, ProgramSource, ProgrammingLanguage) VALUES (?,?,?,?)",submission_value)
        submission_id = c.lastrowid
        c.close()
        self.conn.commit()
        return submission_id



    '''Lookup_signatures looks up signatures which will be used to check for potential cheating or copied code. '''
    def lookup_matching_signatures(self, submission_id):
        return self.signature_manager.lookup_matching_signatures(submission_id)

    '''Data populate is a method used to insert students into the database for testing.'''
    def data_populate(self,student_number, course_code):
        c = self.conn.cursor()
        data_Values = (student_number,course_code)
        c.execute("INSERT INTO Students (StudentNumber, CourseCode) VALUES (?,?,?)",data_Values)
        c.close()
        self.conn.commit()

    def fetch_an_assignment(self,assignmentNumber):
        c = self.conn.cursor()
        c.execute('SELECT Id, CourseCode, AssignmentDescription, DueDate FROM Assignments WHERE Id=?' ,(assignmentNumber, ))
        assignment = None
        for x in c:
            assignment = Assignment(
                id = x[0],
                course_code = x[1],
                description = x[2],
                due_date = x[3]
            )
        c.close()
        return assignment


    def fetch_current_assignments(self):
        c = self.conn.cursor()
        date = time.strftime('%Y-%m-%d')
        c.execute('SELECT Id, CourseCode, AssignmentDescription, DueDate, DueDate < ? FROM Assignments',(date,))
        assignments = []
        for row in c:
            count = self.count_submissions(row[0])
            assignments.append(Assignment(row[0], row[1], row[2], row[3], row[4], count))
        c.close()
        return assignments

    def fetch_a_submission(self, assignment_id, submission_id):
        c = self.conn.cursor()
        c.execute('SELECT Id, StudentId, AssignmentNumber, ProgramSource, SubmissionDate, '
                'ProgrammingLanguage FROM Submissions WHERE AssignmentNumber = ? AND Id = ?',
                (assignment_id, submission_id))
        submission = None
        for x in c:
            submission = Submission(
                    id=x[0],
                    student_number=x[1],
                    program_source=x[3],
                    assignment_id=x[2],
                    submission_date=x[4],
                    language=x[5])
        c.close()
        return submission


    def fetch_submissions(self, assignment_id):
        c = self.conn.cursor()
        submissions = []
        c.execute('SELECT Id, StudentId, AssignmentNumber, ProgramSource, SubmissionDate, '
                'ProgrammingLanguage FROM Submissions WHERE AssignmentNumber = ?' ,(assignment_id, ))
        for x in c:
            submissions.append(
                Submission(
                    id=x[0],
                    student_number=x[1],
                    program_source=x[3],
                    assignment_id=x[2],
                    submission_date=x[4],
                    language=x[5]))
        c.close()
        return submissions

    def fetch_source_codes(self, assignment_id):
        c = self.conn.cursor()
        source_codes = {}
        c.execute('SELECT StudentId, ProgramSource '
                'ProgrammingLanguage FROM Submissions WHERE AssignmentNumber = ?' ,(assignment_id, ))
        for x in c:
            source_codes[x[0]] = x[1]
        c.close()
        return source_codes

    def store_assignment(self,courseCode, assignment_description,due_date):
        c = self.conn.cursor()

        assignmentValues = (assignment_description,due_date,courseCode)

        c.execute('INSERT INTO Assignments (AssignmentDescription,DueDate,CourseCode) VALUES (?,?,?)',assignmentValues)
        assignment_id = c.lastrowid
        c.close()
        self.conn.commit()
        return assignment_id

    def delete_student(self,studentId):
        c = self.conn.cursor()
        c.execute('DELETE FROM Students where StudentNumber=?' ,(studentId, ))
        c.close()
        self.conn.commit()

    def delete_assignment(self, assignmentNumber):
        c = self.conn.cursor()
        c.execute('DELETE FROM Assignments where Id=?' ,(assignmentNumber, ))
        c.execute('DELETE FROM sqlite_sequence WHERE name="Assignments"')
        self.delete_submissions(assignmentNumber)
        c.close()
        self.conn.commit()

    def update_assignment(self, assignmentNumber, courseCode, assignmentDescription, dueDate):
        c = self.conn.cursor()
        c.execute('SELECT * FROM Assignments WHERE Id=?', (assignmentNumber, ))
        for row in c:
            course_code = row[1]
            description = row[2]
        if (courseCode):
            course_code = courseCode
        if (assignmentDescription):
            description = assignmentDescription
        if (dueDate):
            dueDate = dueDate
        c.execute('UPDATE Assignments SET CourseCode="' + course_code + '", AssignmentDescription="' + description + '", DueDate="' + dueDate + '" WHERE ID=' + assignmentNumber + ';')
        c.close()
        self.conn.commit()

    def delete_submissions(self, assignmentNum):
        c = self.conn.cursor()
        c.execute('DELETE FROM Submissions where AssignmentNumber=?' ,(assignmentNum, ))
        c.close()
        self.conn.commit()

    def delete_submission(self,submissionId):
        c = self.conn.cursor()
        c.execute('DELETE FROM Submissions where Id=?' ,(submissionId, ))
        c.close()
        self.conn.commit()

    def count_submissions(self, assignment_num):
        c = self.conn.cursor()
        c.execute('SELECT Count(*) FROM Submissions WHERE AssignmentNumber=?' ,(assignment_num, ))
        count = c.fetchone()[0]
        c.close()
        return count

    def delete_signatures(self,signatureId):
        c = self.conn.cursor()
        c.execute('DELETE FROM Signatures where Id=?' ,(signatureId, ))
        c.close()
        self.conn.commit()

    def update_assignment(self,id, courseCode, description, dueDate):
        self.conn.execute('UPDATE Assignments SET CourseCode = ?, AssignmentDescription = ?, DueDate = ? Where Id = ?',
                          (courseCode,description,dueDate,id))
        self.conn.commit()
        self.conn.close()

    def fetch_max_submission_id(self):
        c = self.conn.cursor()
        c.execute('SELECT MAX(Id) FROM Submissions')
        max_id = c.fetchone()[0]
        c.close()
        return max_id

    def fetch_max_submission_match_id(self):
        c = self.conn.cursor()
        c.execute('SELECT MAX(SubmissionId) FROM SubmissionMatches')
        max_id = c.fetchone()[0]
        c.close()
        return max_id

    def fetch_submission_match(self, submission_id):
        c = self.conn.cursor()
        c.execute('SELECT Id, SubmissionId, MatchSubmissionId, NumberSignaturesMatched, Confidence '
                'FROM SubmissionMatches WHERE SubmissionId = ?', (submission_id, ))
        row = c.fetchone()
        match = None
        if row:
            match = SignatureMatch(*row)
        c.close()

        return match

    def update_submission_match(self, signature_match, match_submission_id, number_signatures_matched):
        c = self.conn.cursor()
        c.execute('UPDATE SubmissionMatches SET MatchSubmissionId = ?, NumberSignaturesMatched = ?, '
                  'Confidence=(SELECT ? / length(ProgramSource) FROM Submissions WHERE Id = ? LIMIT 1)'
                'WHERE SubmissionId = ?',
                (match_submission_id, number_signatures_matched, number_signatures_matched,
                 signature_match.submission_id, signature_match.submission_id))
        c.close()
        self.conn.commit()

    def store_submission_match(self, submission_id, other_submission_id, number_signatures_match):
        c = self.conn.cursor()
        c.execute('INSERT INTO SubmissionMatches (SubmissionId, MatchSubmissionId, NumberSignaturesMatched, Confidence)'
                ' VALUES (?, ?, ?, (SELECT ?*100 / length(ProgramSource) FROM Submissions WHERE id = ? LIMIT 1))',
                (submission_id, other_submission_id, number_signatures_match, number_signatures_match, submission_id))
        c.close()
        self.conn.commit()

    def fetch_all_submission_matches(self, assignment_num):
        c = self.conn.cursor()
        c.execute('SELECT sm.Id, sm.SubmissionId, sm.MatchSubmissionId, NumberSignaturesMatched, Confidence, '
                's.StudentId, s2.StudentId FROM SubmissionMatches sm'
                ' JOIN Submissions s ON sm.SubmissionId = s.Id JOIN Submissions s2 ON sm.MatchSubmissionId = s2.Id WHERE s.AssignmentNumber = ? AND s2.AssignmentNumber = ?'
                ' ORDER BY NumberSignaturesMatched DESC',
                (assignment_num, assignment_num))
        results = []
        for row in c:
            results.append(SignatureMatch(*row))
        c.close()
        return results

    def fetch_report(self, assignment_num):
        c = self.conn.cursor()
        c.execute('SELECT * FROM Reports WHERE AssignmentNumber=?', (assignment_num, ))
        results = []
        for row in c:
            results.append(row[1])
        c.close()
        return results

    def insert_report_item(self, assignment_num, student_num):
        c = self.conn.cursor()
        c.execute('INSERT INTO Reports (StudentNumber, AssignmentNumber) VALUES (?,?)', (student_num, assignment_num, ))
        c.close()
        self.conn.commit()

    def delete_report_items(self, assignment_num, student_nums):
        c = self.conn.cursor()
        student_nums = ','.join(map("'{0}'".format, student_nums))
        query = 'DELETE FROM Reports WHERE AssignmentNumber=%s AND StudentNumber IN (%s)' % (assignment_num, student_nums)
        c.execute(query)
        c.close()
        self.conn.commit()

    def count_cheaters(self, assignment_num):
        c = self.conn.cursor()
        c.execute('SELECT Count(*) FROM Reports WHERE AssignmentNumber=?' ,(assignment_num, ))
        count = c.fetchone()[0]
        c.close()
        return count

