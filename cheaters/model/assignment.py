class Assignment:
    id = None
    course_code = None
    description = None
    dueDate = None
    submissions_count = None

    def __init__(self, id, course_code, description,due_date=None, completed=False, submissions_count=None):
        self.id = id
        self.course_code = course_code
        self.description = description
        self.dueDate = due_date
        self.completed = completed
        self.submissions_count = submissions_count

    def __repr__(self):
        return '<Assignment id:%s course_code:%s description:%s dueDate:%s>' % (self.id, self.course_code, self.description,self.dueDate)
