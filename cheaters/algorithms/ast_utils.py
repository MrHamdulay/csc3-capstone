import ast
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
  lineno = node.lineno
  for node in ast.walk(node):
    if hasattr(node, 'lineno'):
      lineno = f(lineno, node.lineno)

  return lineno


def getCodeFromNode(program, node):
  bottom, top = getLineNo(node, True), getLineNo(node, False)

  try:
    return '\n'.join(program.program_source.split('\n')[bottom-1:top+1])
  except:
    return ''
