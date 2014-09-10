import ast
from keyword import kwlist as PYTHON_KWLIST
from collections import defaultdict
from utils import Counter
from languages.python.ast_utils import getLineLimits
import external.unparser
from StringIO import StringIO

from programsubmission import ProgramSubmission
from algorithms.base import SectionMatch


CO_FUTURE_DIVISION   = 0x2000   # division
CO_FUTURE_ABSOLUTE_IMPORT = 0x4000 # perform absolute imports by default
CO_FUTURE_WITH_STATEMENT  = 0x8000   # with statement
CO_FUTURE_PRINT_FUNCTION  = 0x10000   # print function
CO_FUTURE_UNICODE_LITERALS = 0x20000 # unicode string literals

PYTHON3_FLAGS = CO_FUTURE_DIVISION | CO_FUTURE_ABSOLUTE_IMPORT | CO_FUTURE_WITH_STATEMENT | CO_FUTURE_PRINT_FUNCTION | CO_FUTURE_UNICODE_LITERALS | ast.PyCF_ONLY_AST


class RenamerTransform(ast.NodeTransformer):
    ''' ast transform that removes variable names,
    strings and function names to make matching easier

    use: RenamerTransform().visit(ast_node)

    methods of form visit_`type' are called when we
    arrive at a node of type `type' and return
    the node that we wish to replace it with.
    '''

    def visit_Name(self, node):
        #self.generic_visit(node)
        return ast.copy_location(
            ast.Name(
              id='i',#self.name_map[node.id],
              ctx=node.ctx),
            node)

    def visit_Str(self, node):
        #self.generic_visit(node)
        return ast.copy_location(ast.Str(s='s'), node)

    def visit_FunctionDef(self, node):
        self.generic_visit(node)
        return ast.copy_location(
            ast.FunctionDef(
                'f',#self.name_map[node.name],
                node.args,
                node.body,
                node.decorator_list),
            node)

    #this should strip out the function name when calling methods on a class
    #def visit_Call(self, node):
    #    call = ast.Call(
    #            args=node.args,


class PythonLanguageHandler(ProgramSubmission):
  file_types = ['py']

  def parse_file(self, program_source, filename=''):
    ProgramSubmission.parse_file(self, program_source, filename)
    # let's try to compile python 3 code first
    try:
        self.ast = compile(program_source, '<unknown>', 'exec', PYTHON3_FLAGS)
    except SyntaxError:
        self.ast = ast.parse(program_source)


  '''
  mark a section of code as having being cheated
  from someone'''
  def mark_cheated(self, node):
    # reevaluate this when we mark more things
    self.cheated_sections = None
    if isinstance(node, SectionMatch):
      bottom, top = node.startline, node.endline
    else:
      bottom, top = getLineLimits(node)
    for i in xrange(bottom, top):
      self.potential_cheated_sections[i] = True

  ''' print the source of a given node '''
  def print_node(self, node):
    bottom, top = getLineLimits(node)
    print '\n'.join(self.program_source.split('\n')[bottom:top])

  ''' return an AST with variable names etc removed '''
  @property
  def canonicalised_ast(self):
    return RenamerTransform().visit(self.ast)

  ''' return the program source with variable names etc removed'''
  def strip_unstable_atrributes(self):
    buf = StringIO()
    external.unparser.Unparser(self.canonicalised_ast, buf)
    result = buf.getvalue()
    # remove tab indentation, we don't care about that
    result = '\n'.join(x.strip() for x in result.split('\n'))
    # shorten python keywords so ngrams aren't affected by keywords like 'print' with 'pri'
    for key in PYTHON_KWLIST:
        result = result.replace(key, key[:3])
    return result
