from collections import defaultdict, Iterable
from copy import deepcopy
import ast

from algorithms.base import BaseAlgorithm
from algorithms.ast_utils import *

class RenamerTransform(ast.NodeTransformer):
    def __init__(self):
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
    def __init__(self, program_source):
        self.program_source = program_source
        self.ast = ast.parse(program_source)


class TreeHash(BaseAlgorithm):
    def __init__(self):
        self.program_hashes = {}
        self.copied_instances = []


    def isPlagiarised(self, program):
        if isinstance(program, str):
            program = PythonProgram(program)

        for node in ast.walk(program.ast):
          if isinstance(node, (ast.Module, ast.FunctionDef)):
            # get rid of all the painful variables
            # deepcopy the nodes. may be a performance problem but should be fine
            devariabled = RenamerTransform().visit(deepcopy(node))
            h = hash(str(ast.dump(devariabled)))
            if h in self.program_hashes:
                print 'we found some copies! \nSTART'
                print getCodeFromNode(program, node)
                print 'END!\n Original'
                print getCodeFromNode(*self.program_hashes[h])
                print 'END!'
                print
                #print ast.dump(node, True, True)
                self.copied_instances.append(node)
            else:
                self.program_hashes[h] = (program, node)

