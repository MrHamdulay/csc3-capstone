from languages.python import PythonProgram
code = '''
print 'hello world'

class A:
  def first_function(self, a):
    a *= 2
    if isinstance(a, int):
      print 'This most definitely gets executed for sure'

    return first_function

def second_function(b):
  b = 2
  for i in xrange(1000):
    first_function(i)
    b = 2
    for i in xrange(1000):
      first_function(i)

b = 2
for i in xrange(1000):
  first_function(i)'''
expected='''print 's'

class A:
    def f(i, i):
        i *= 2
        if i(i, i):
            print 's'

        return i

def f(i):
    i = 2
    for i in i(1000):
        i(i)
        i = 2
        for i in i(1000):
            i(i)

i = 2
for i in i(1000):
    i(i)'''

program = PythonProgram(code, 'a.py')
assert program.get_canonicalised_program_source.strip() == expected.strip()
