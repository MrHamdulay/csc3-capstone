MIN_CHEAT_LENGTH = 1

class Program:
    def __init__(self, program_source, filename=''):
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
    def get_canonicalised_program_source(self):
      raise NotImplemented

    def mark_cheated(self, section):
      raise NotImplemented


    ''' a rather boring line by line cheat evaluator'''
    def evaluate_cheated(self):
      potentials = self.potential_cheated_sections
      self.cheated_sections = [False]*len(potentials)
      i = 0
      while i < len(potentials):
        current_run_len = 0
        start_run = i
        if i < len(potentials) and potentials[i]:
          while i < len(potentials) and potentials[i]:
            i += 1
            # do not count blank lines
            if len(self.program_source[i].strip()):
              current_run_len += 1
        else:
          i += 1
        # this should probably be a function of the complexity of the AST
        # but this works for now
        if current_run_len >= MIN_CHEAT_LENGTH :
          for j in xrange(start_run, start_run+current_run_len):
            self.cheated_sections[j] = True


    '''
    return a (posix) string representation of the program source that
    highlights all sections of the code that we have detected
    as being copied from someone
    '''
    @property
    def listing(self):
      if self.cheated_sections is None:
        self.evaluate_cheated()

      string = ''

      for i, line in enumerate(self.program_source.split('\n')):
        if self.cheated_sections[i]:
          string += '\033[92m'
        string += line+'\n'
        if self.cheated_sections[i]:
          string += '\033[0m'
      return string