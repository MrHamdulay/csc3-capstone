from collections import defaultdict, Iterable
from copy import deepcopy
import ast

from algorithms.base import BaseAlgorithm
from algorithms.ast_utils import *

class RenamerTransform(ast.NodeTransformer):
    def __init__(self):
        # it turns out that the name map is only used when checking
        # for equality, not when we are hashing. It's too strict
        self.name_map = defaultdict(Counter())

    def visit_Name(self, node):
        self.generic_visit(node)
        return ast.copy_location(
            ast.Name(
              id='asdf',#self.name_map[node.id],
              ctx=node.ctx),
            node)

    def visit_FunctionDef(self, node):
        self.generic_visit(node)
        return ast.copy_location(
            ast.FunctionDef(
                'asdf',#self.name_map[node.name],
                node.body,
                node.args,
                node.decorator_list),
            node)


class PythonProgram:
    def __init__(self, program_source, filename=''):
        self.filename=filename
        self.program_source = program_source
        self.ast = ast.parse(program_source)


BLOCKCLASSES = (ast.Module, ast.FunctionDef, ast.For, ast.If, ast.While)

class TreeHash(BaseAlgorithm):
    def __init__(self):
        self.program_hashes = {}
        self.copied_instances = []


    def isPlagiarised(self, program):
        if isinstance(program, str):
            program = PythonProgram(program)

        for node in ast.walk(program.ast):
          if isinstance(node, BLOCKCLASSES):
            # get rid of all the painful variables
            # deepcopy the nodes. may be a performance problem but should be fine
            devariabled = RenamerTransform().visit(deepcopy(node))
            h = hash(str(ast.dump(devariabled)))
            if h in self.program_hashes:
                print 'we found some copies! daaaamn.\n original (%s) \n \033[1;31m' % program.filename
                print getCodeFromNode(program, node)
                print '\033[1;m\ncopied from (%s)\n \033[1;32m' % (self.program_hashes[h][0].filename)
                print getCodeFromNode(*self.program_hashes[h])
                print '\033[1;m'
                print
                #print ast.dump(node, True, True)
                self.copied_instances.append(node)
            else:
                self.program_hashes[h] = (program, node)

