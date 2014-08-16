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
program = PythonProgram(code, 'a.py')
print program.get_canonicalised_program_source
