class Match:
    submission_id = None
    start_line = None
    match_length = None
    number_of_signatures = None

    def __init__(self, submission_id, start_line, match_length, number_of_signatures=0):
        self.submission_id = submission_id
        self.start_line = start_line
        self.match_length = match_length
        self.number_of_signatures = number_of_signatures

    def __repr__(self):
        return '<Match submission_id:%s start_line:%s match_length:%s>' % (self.submission_id, self.start_line, self.match_length)
