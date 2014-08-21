class Assignment:
    id = None
    course_code = None
    description = None

    def __init__(self, id, course_code, description):
        self.id = id
        self.course_code = course_code
        self.description = description

    def __repr__(self):
        return '<Assignment id:%s course_code:%s description:%s>' % (self.id, self.course_code, self.description)
