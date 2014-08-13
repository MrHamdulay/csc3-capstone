from collections import defaultdict, Iterable
import sys
from copy import deepcopy
import ast

from algorithms.base import BaseAlgorithm
from algorithms.ast_utils import *
from program import Program

class PythonProgram(Program):
  def __init__(self, program_source, filename=''):
    Program.__init__(self, program_source, filename)
    self.ast = ast.parse(program_source)
    print 'programs ast'
    print ast.dump(self.ast)
    print


  def mark_cheated(self, node):
    # reevaluate this when we mark more things
    self.cheated_sections = None
    bottom, top = getLineLimits(node)
    for i in xrange(bottom, top):
      self.potential_cheated_sections[i] = True

  def print_node(self, node):
    bottom, top = getLineLimits(node)
    print '\n'.join(self.program_source.split('\n')[bottom:top])

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



class TreeHash(BaseAlgorithm):
    def __init__(self):
        self.program_hashes = defaultdict(list)
        self.new_hashes = defaultdict(list)

    def isPlagiarised(self, program):
        if isinstance(program, str):
            program = PythonProgram(program)

        # remove all variable anf function names from ast
        devariabled = RenamerTransform().visit(program.ast)
        for node in ast.walk(devariabled):
          # get rid of all the painful variables
          # deepcopy the nodes. may be a performance problem but should be fine
          if len(list(ast.walk(node))) < 4:
            continue
          if isinstance(node, IGNORE_AST):
            #print 'ignored', type(node)
            continue
          print type(node), len(list(ast.walk(node))), ast.dump(node)[:90]
          h = str(ast.dump(node))
          node.cheated = h in self.program_hashes
          if h in self.program_hashes:
              if True:
                  print '\033[92m', self.program_hashes[h][0][0].filename,'\033[0m new listing. This came from '
                  print h
                  sys.stdout.write( '\033[92m')
                  self.program_hashes[h][0][0].print_node(self.program_hashes[h][0][1])
                  sys.stdout.write( '\033[0m')
                  print '\033[92m',program.filename,'\033[0m and then'
                  print ast.dump(self.program_hashes[h][0][1])
                  sys.stdout.write( '\033[94m')
                  program.print_node(node)
                  sys.stdout.write( '\033[0m')
                  print
                  print

              for (oProgram, oNode) in self.program_hashes[h]:
                  oProgram.mark_cheated(oNode)

              program.mark_cheated(node)
          else:
              # store for next time (don't add it to the thing we look up to prevent
              # self cheating
              self.new_hashes[h].append((program, node))

        self.program_hashes.update(self.new_hashes)
        self.new_hashes = defaultdict(list)



