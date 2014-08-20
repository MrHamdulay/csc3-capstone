class Submission:
    id = None
    studentId = None
    program_Source = None
    assignment_Number = None
    submissionDate = None

    def __init__(self,iD,student_id, programSource, assignmentNumber, submission_date):
        self.id = iD
        self.studentId = student_id
        self.program_Source = programSource
        self.assignment_Number=assignmentNumber
        self.submissionDate = submission_date