import ast
from collections import defaultdict
from utils import Counter
from .ast_utils import getLineLimits

from program import Program

class RenamerTransform(ast.NodeTransformer):
    def __init__(self):
        # it turns out that the name map is only used when checking
        # for equality, not when we are hashing. It's too strict
        self.name_map = defaultdict(Counter())

    def visit_Name(self, node):
        self.generic_visit(node)
        return ast.copy_location(
            ast.Name(
              id='',#self.name_map[node.id],
              ctx=node.ctx),
            node)

    def visit_Str(self, node):
        self.generic_visit(node)
        return ast.copy_location(ast.Str(s=''), node)

    def visit_FunctionDef(self, node):
        self.generic_visit(node)
        return ast.copy_location(
            ast.FunctionDef(
                '',#self.name_map[node.name],
                node.body,
                node.args,
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


  def mark_cheated(self, node):
    # reevaluate this when we mark more things
    self.cheated_sections = None
    bottom, top = getLineLimits(node)
    for i in xrange(bottom, top):
      self.potential_cheated_sections[i] = True

  def print_node(self, node):
    bottom, top = getLineLimits(node)
    print '\n'.join(self.program_source.split('\n')[bottom:top])

  @property
  def canonicalised_ast(self):
    return RenamerTransform().visit(self.ast)

  @property
  def get_canonicalised_program_source(self):
    return str(ast.dump(self.canonicalised_ast))
