import ast
from external.unparser import Unparser
from StringIO import StringIO

code = '''
a = 5


def f():

    pass

b = 6'''
code_ast = ast.parse(code)
buf = StringIO()
Unparser(code_ast, buf)
assert buf.getvalue().strip() == code.strip()
