import ast
from collections import defaultdict
from utils import Counter
from languages.python.ast_utils import getLineLimits
import external.unparser
from StringIO import StringIO

from program import Program


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


class PythonProgram(Program):
  def __init__(self, program_source, filename=''):
    Program.__init__(self, program_source, filename)
    self.ast = ast.parse(program_source)


  '''
  mark a section of code as having being cheated
  from someone'''
  def mark_cheated(self, node):
    # reevaluate this when we mark more things
    self.cheated_sections = None
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
  @property
  def get_canonicalised_program_source(self):
    buf = StringIO()
    external.unparser.Unparser(self.canonicalised_ast, buf)
    return buf.getvalue()
