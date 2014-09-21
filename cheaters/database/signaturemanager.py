'''Authors: Jarred De Beer, Yaseen Hamdulay & Merishka Lalla
Date: 22/9/2014
Signature manager class
'''

from collections import defaultdict
from model.signature import Signature

'''SignatureManager is a class used to assist the DatabaseManager with the format needed for signatures to be in for comparitive reasons'''

class SignatureManager:
    def __init__(self):
        self.submission_to_ngram = defaultdict(list)
        self.ngram_to_submission = defaultdict(list)
        self.signatures = {}

    '''store_signatures is a method which stores a signature with all relevant data.'''

    def store_signature(self, s, submission_id):
        submission_id = int(submission_id)
        self.submission_to_ngram[submission_id].append(s.ngram_hash)
        self.ngram_to_submission[s.ngram_hash].append(submission_id)
        self.signatures[(submission_id, s.ngram_hash)] = s

    '''lookup_matching_signatures finds all signatures with a matching structure based on ngram hashing. A set is then made and
    returned'''

    def lookup_matching_signatures(self, submission_id):
        submission_id = int(submission_id)
        matching = set()
        for ngram in self.submission_to_ngram[submission_id]:
            sig = self.signatures[submission_id, ngram]
            for o_submission_id in self.ngram_to_submission[ngram]:
                if submission_id == o_submission_id:
                    continue
                sig2 = self.signatures[o_submission_id, ngram]
                signature = Signature(
                        sig.ngram_hash, sig.submission_id_mine, sig.line_number_mine,
                        sig2.submission_id_mine, sig2.line_number_mine)
                matching.add(signature)
        return matching
