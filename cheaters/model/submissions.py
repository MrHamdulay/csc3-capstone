class Submission:
    id = None
    student_number = None
    program_source = None
    assignment_id = None
    submissionDate = None

    def __init__(self,id,student_number, program_source, assignment_id, submission_date):
        self.id = id
        self.student_number = student_number
        self.program_source = program_source
        self.assignment_id = assignment_id
        self.submission_date = submission_date
