import ast
from external.unparser import Unparser
program = '''
world = 5

#things
'stuffs'
print 'world''''
expected = '''
world = 5


'stuffs'
print 'world''''
