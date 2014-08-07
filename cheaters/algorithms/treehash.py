from collections import defaultdict, Iterable
from copy import deepcopy
import ast

from algorithms.base import BaseAlgorithm
from algorithms.ast_utils import *

class RenamerTransform(ast.NodeTransformer):
    def __init__(self):
        self.name_map = defaultdict(Counter())

    def visit_Name(self, node):
        return ast.Name(id=self.name_map[node.id], ctx=node.ctx)

    def visit_FunctionDef(self, node):
        return ast.FunctionDef(
                self.name_map[node.name],
                node.body,
                node.args,
                node.decorator_list)

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
            # get rid of all the painful variables
            # deepcopy the nodes. may be a performance problem but should be fine
            devariabled = RenamerTransform().visit(deepcopy(node))
            h = astHash(devariabled)
            if h in self.program_hashes:
                self.copied_instances.append(node)
                print 'potential equality'
            else:
                self.program_hashes[h] = (program, node)

