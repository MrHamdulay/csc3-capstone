'''
Author: Yaseen Hamdulay, Jarred de Beer, Merishka Lalla
Date: 15 August 2014

Cache of db storage for signatures
'''
from collections import defaultdict
from model.signature import Signature

class SignatureManager:
    def __init__(self):
        self.submission_to_ngram = defaultdict(list)
        self.ngram_to_submission = defaultdict(list)
        self.signatures = {}

    def store_signature(self, s, submission_id):
        submission_id = int(submission_id)
        self.submission_to_ngram[submission_id].append(s.ngram_hash)
        self.ngram_to_submission[s.ngram_hash].append(submission_id)
        self.signatures[(submission_id, s.ngram_hash)] = s

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
