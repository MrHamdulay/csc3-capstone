from collections import defaultdict, Iterable
import sys
from copy import deepcopy
import ast

from algorithms.base import BaseAlgorithm
from program import Program


class TreeHash(BaseAlgorithm):
    ALLOWED_LANGUAGE_EXTENSIONS = ['py']

    def __init__(self):
        self.program_hashes = defaultdict(list)
        self.new_hashes = defaultdict(list)

    def isPlagiarised(self, program):

        # remove all variable and function names from ast
        devariabled = program.canonicalised_ast
        for node in ast.walk(devariabled):
          # get rid of all the painful variables
          # deepcopy the nodes. may be a performance problem but should be fine
          if len(list(ast.walk(node))) < 3:
            h = str(ast.dump(node))
            continue

          if isinstance(node, IGNORE_AST):
            continue

          h = str(ast.dump(node))
          node.cheated = h in self.program_hashes
          if h in self.program_hashes:
              #if False:
              #    print '\033[92m', self.program_hashes[h][0][0].filename,'\033[0m new listing. This came from '
              #    print h
              #    sys.stdout.write( '\033[92m')
              #    self.program_hashes[h][0][0].print_node(self.program_hashes[h][0][1])
              #    sys.stdout.write( '\033[0m')
              #    print '\033[92m',program.filename,'\033[0m and then'
              #    print ast.dump(self.program_hashes[h][0][1])
              #    sys.stdout.write( '\033[94m')
              #    program.print_node(node)
              #    sys.stdout.write( '\033[0m')
              #    print
              #    print

              for (oProgram, oNode) in self.program_hashes[h]:
                  oProgram.mark_cheated(oNode)

              program.mark_cheated(node)
          # store for next time (don't add it to the thing we look up to prevent
          # self cheating
          self.new_hashes[h].append((program, node))

        self.program_hashes.update(self.new_hashes)
        self.new_hashes = defaultdict(list)



