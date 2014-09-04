class Student:

    id = None
    course_code = None
    student_number = None

    def __init__(self, id, student_number, course_code):
        self.id = id
        self.course_code = course_code
        self.student_number = student_number

    def __repr__(self):
        return '<Student id:%s course_code:%s student_number:%s>' % (self.id, self.course_code, self.student_number)
