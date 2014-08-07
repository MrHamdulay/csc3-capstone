print 'hello world'

def first_function(a):
  a *= 2
  if isinstance(a, int):
    print 'This most definitely gets executed for sure'

  return first_function

b = 2
for i in xrange(1000):
  first_function(i)
