'''
Author: Yaseen Hamdulay, Jarred de Beer, Merishka Lalla
Date: 15 August 2014
'''


''' generic/ abstract class that represents a program subimssion.
'''
class ProgramSubmission:
    def parse_file(self, program_source, filename=''):
        self.filename=filename
        self.program_source = program_source
        self.potential_cheated_sections = [False]*len(program_source.split('\n'))
        self.cheated_sections = None

    def __repr__(self):
      return '<Program file:%s len:%s>' % (self.filename, len(self.program_source))

    '''
    return a version of the program source
    with all variable names, strings, class names etc
    removed. This removes the potential for simple
    replacements to deceive us'''
    @property
    def get_canonicalised_program_source(self):
      raise NotImplemented

