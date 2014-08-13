import ast
import _ast


BLOCKCLASSES_AST = (ast.Module, ast.FunctionDef, ast.For, ast.If, ast.While)

IGNORE_AST = (_ast.Store, _ast.Name, _ast.Load, _ast.Store, _ast.Del, _ast.Str, _ast.Num, _ast.arguments, _ast.Load, _ast.Mult, _ast.Ellipsis, _ast.Attribute)

def Counter():
    count = 0
    def counterer():
        counterer.count += 1
        return counterer.count
    counterer.count = 0
    return counterer

#MAGIC

def determinstic_iter_fields(node):
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

def getLineNo(node, bottom):
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
  return getLineNo(node, True)-1, getLineNo(node, False)


def getCodeFromNode(program, node):
  bottom, top = getLineLimits(node)

  try:
    return '\n'.join(program.program_source.split('\n')[bottom:top])
  except:
    return ''
