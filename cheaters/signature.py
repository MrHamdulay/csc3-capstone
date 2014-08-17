class Signature:
    '''
    Identifies common structure between code '''


    submission_id = None
    ngram_hash = None
    line_number = None

    def __init__(self, ngram_hash, submission_id, line_number):
        self.ngram_hash = ngram_hash
        self.submission_id = submission_id
        self.line_number = line_number

