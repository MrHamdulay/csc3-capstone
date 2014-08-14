class BaseAlgorithm:
  ALLOWED_LANGUAGES = ['py']

  '''
  @param program string source code of the program we are checking for cheating
  @returns double confidence that the given program is plagiarised
  '''
  def isPlagiarised(self, program):
    raise NotImplemented('This method is not implemented yet')



