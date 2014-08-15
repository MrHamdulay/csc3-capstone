from collections import defaultdict, Iterable
import sys
from copy import deepcopy
import ast

from algorithms.base import BaseAlgorithm
from program import Program
from languages.python.ast_utils import IGNORE_AST


class TreeHash(BaseAlgorithm):
    ALLOWED_LANGUAGE_EXTENSIONS = ['py']

    def __init__(self):
        # maps ast nodes to the program
        self.program_hashes = defaultdict(list)
        # temp map of above for current program
        self.new_hashes = defaultdict(list)

    def isPlagiarised(self, program):

        # remove all variable and function names from ast
        devariabled = program.canonicalised_ast

        # go through all nodes
        for node in ast.walk(devariabled):
          # get rid of all the painful variables
          # deepcopy the nodes. may be a performance problem but should be fine
          if len(list(ast.walk(node))) < 3:
            h = str(ast.dump(node))
            continue

          # ignore things like constants, etc
          if isinstance(node, IGNORE_AST):
            continue


          # convert to a nice representation that we can store
          h = str(ast.dump(node))

          node.cheated = h in self.program_hashes
          if node.cheated:
              # tell all other instances of the program that they have cheated at a point
              for (oProgram, oNode) in self.program_hashes[h]:
                  oProgram.mark_cheated(oNode)

              # mark the current node as having being cheated
              program.mark_cheated(node)
          # store for next time (don't add it to the thing we look up to prevent
          # self cheating
          self.new_hashes[h].append((program, node))


        # update our list of hashes
        self.program_hashes.update(self.new_hashes)
        self.new_hashes = defaultdict(list)



