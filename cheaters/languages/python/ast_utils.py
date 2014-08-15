import ast
import _ast


# ast nodes that start new blocks
BLOCKCLASSES_AST = (ast.Module, ast.FunctionDef, ast.For, ast.If, ast.While)

# ast nodes that we don't care about
IGNORE_AST = (_ast.Store, _ast.Name, _ast.Load, _ast.Store, _ast.Del, _ast.Str, _ast.Num, _ast.arguments, _ast.Load, _ast.Mult, _ast.Ellipsis, _ast.Attribute)


def Counter():
    ''' helper function that returns a function that
    increments from 0 to infinity
    @returns lambda that upon getting called returns integer from 1 .. inf
    '''
    count = 0
    def counterer():
        counterer.count += 1
        return counterer.count
    counterer.count = 0
    return counterer

#MAGIC

def determinstic_iter_fields(node):
    ''' given a node return all it's children in sorted order'''
    if not hasattr(node, '_fields'):
      return
    for field in sorted(node._fields):
        try:
            f = getattr(node, field)
            if isinstance(f, list):
                f = sorted(f)
            yield field, f
        except AttributeError:
            pass

#monkey patch the ast class to give us a deterministic order on fields (and then also child nodes)
ast.iter_fields = determinstic_iter_fields

def astHash(iterable):
    ''' given an AST node return a hash of it '''
    h = 0x456789
    if isinstance(iterable, ast.AST):
        return astHash(determinstic_iter_fields(iterable))
    if isinstance(iterable, (int, basestring)):
        return hash(field)

    for field in iterable:
        t_hash = 0
        if isinstance(field, (int, basestring)):
            t_hash = hash(field)
        elif isinstance(field, (list, tuple)):
            t_hash = astHash(field)
        elif isinstance(field, dict):
            t_hash = astHash(field.itervalues())

        h ^= t_hash

    return h

def getLineNo(node, bottom=True):
  ''' return the top or bottom line nubmer of an AST node
  @param node ast.node node to find line limits of
  @param bottom true if we're finding the bottom limit, false if we're finding the top
  @return int corresponding line number'''

  f = min if bottom else max
  try:
    lineno = node.lineno
  except:
    lineno = 10000 if bottom else -10000
  for node in ast.walk(node):
    if hasattr(node, 'lineno'):
      lineno = f(lineno, node.lineno)

  return lineno

def getLineLimits(node):
  ''' find the bottom and top line number of an ast node

  @param node ast.node node to find limtis of
  @return (int, int) line limits'''
  return getLineNo(node, True)-1, getLineNo(node, False)+1


def getCodeFromNode(program, node):
  ''' return the program source
  @param program original program object
  @param node section of program source that we wish to return the source of
  @return string program source for corresponding node '''
  bottom, top = getLineLimits(node)

  try:
    return '\n'.join(program.program_source.split('\n')[bottom:top])
  except:
    return ''
