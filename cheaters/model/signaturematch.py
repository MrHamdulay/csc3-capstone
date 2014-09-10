class SignatureMatch:
    def __init__(self, id, submission_id, match_submission_id, number_signatures_matched, confidence):
      self.id = id
      self.submission_id = submission_id
      self.match_submission_id = match_submission_id
      self.number_signatures_matched = number_signatures_matched
      self.confidence = confidence
