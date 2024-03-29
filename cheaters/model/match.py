'''
Author: Yaseen Hamdulay, Jarred de Beer, Merishka Lalla
Date: 15 August 2014

Python object that represents a row in the Matches database table
'''


class Match:
    submission_id = None
    start_line = None
    match_length = None
    number_of_signatures = None

    def __init__(self, submission_id, start_line_mine, match_length, number_of_signatures):
        self.submission_id = submission_id
        self.start_line_mine = start_line_mine
        self.match_length = match_length
        self.number_of_signatures = number_of_signatures

    def __repr__(self):
        return '<Match their_submission_id:%s my_start_line:%s match_length:%s (%d)>' % (self.submission_id, self.start_line_mine, self.match_length, self.number_of_signatures)

