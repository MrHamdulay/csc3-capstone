#__author__ = 'Merishka Lalla'
import os
import sqlite3
from model.signature import Signature
from model.assignment import Assignment


class DatabaseManager:
    conn = None

    def __init__(self, database_file='cheaters.db'):
        self.conn = sqlite3.connect(database_file)
        self.initialise_database()


    def initialise_database(self):
        c = self.conn.cursor()
        file = open(os.path.dirname(os.path.realpath(__file__))+'/schema.sql','r')
        c.executescript(file.read())
        c.close()
        self.conn.commit()


    def store_signatures(self,signatures,submission_id):
        c = self.conn.cursor()
        for s in signatures:
            signature_values = (s.line_number,s.ngram_hash, submission_id)
            c.execute("INSERT INTO Signatures(LineNumber,NgramHash,SubmissionId) VALUES(?,?,?)",signature_values)
        c.close()
        self.conn.commit()

    def store_submissions(self,concatenated_file, assignment_number):
        c = self.conn.cursor()
        submission_value = (1,concatenated_file,assignment_number)

        c.execute("INSERT INTO Submissions (StudentId,AssignmentNumber, ProgramSource) VALUES (?,?,?)",submission_value)
        submission_id = c.lastrowid
        c.close()
        self.conn.commit()
        return submission_id

    def store_matches(self,grouped_matches):
        c = self.conn.cursor()

    def lookup_signatures(self, submission_id):
        c = self.conn.cursor()
        c.execute('SELECT SubmissionId, NgramHash FROM Signatures WHERE SubmissionId != ?'
        'AND NgramHash IN (SELECT NgramHash FROM Signatures WHERE SubmissionId = ?)', (submission_id, submission_id))
        signatures = [row for row in c]
        c.close()
        return signatures

    def fetch_current_assignments(self):
        c = self.conn.cursor()
        c.execute('SELECT Id, CourseCode, AssignmentDescription FROM Assignments')# WHERE DueDate >= CURRENT_DATE')
        assignments = []
        for row in c:
            assignments.append(Assignment(*row))
        c.close()
        print assignments
        return assignments
