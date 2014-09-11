class SignatureMatch:
    def __init__(self, id, submission_id, match_submission_id, number_signatures_matched, confidence, student_number1=None, student_number2=None):
      self.id = id
      self.submission_id = submission_id
      self.match_submission_id = match_submission_id
      self.number_signatures_matched = number_signatures_matched
      self.confidence = confidence
      self.student_number1 = student_number1
      self.student_number2 = student_number2

    def apiify(self):
        return {
          'source': str(self.student_number1),
          'target': str(self.student_number2),
          'source_id': str(self.submission_id),
          'target_id': str(self.match_submission_id),
          'confidence': str(self.number_signatures_matched)
        }
