'''
Author: Yaseen Hamdulay, Jarred de Beer, Merishka Lalla
Date: 15 August 2014

Python object that represents a row in the Signatures database table
'''

class Signature:
    '''
    Identifies common structure between code '''


    submission_id_mine = None
    submission_id_theirs = None
    ngram_hash = None
    line_number_mine = None
    line_number_theirs = None

    def __init__(self, ngram_hash, submission_id_mine, line_number, submission_id_theirs=None, line_number_theirs=None):
        self.ngram_hash = ngram_hash
        self.submission_id_mine = submission_id_mine
        self.line_number_mine = line_number
        self.submission_id_theirs = submission_id_theirs
        self.line_number_theirs = line_number_theirs
        assert submission_id_mine != submission_id_theirs or submission_id_mine is None

    def reverse(self):
        assert self.line_number_theirs
        return Signature(self.ngram_hash, self.submission_id_theirs, self.line_number_theirs, self.submission_id_mine, self.line_number_mine)

    def __repr__(self):
        return '<Signature hash:"%s" id:%s line_number:%s their_line_number:%s %s %s>' % (self.ngram_hash, self.submission_id_mine, self.line_number_mine, self.line_number_theirs, self.submission_id_mine, self.submission_id_theirs)
