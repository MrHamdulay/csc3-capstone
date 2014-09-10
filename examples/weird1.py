print 'hello world'

def unrelate_function(a, b, c):
    print 'among other things'
    (x for x in xrange(1000))
    for z in range(123):
        a = b*2+3
        print 'hello hello hello hello'
        unrelate_function(1,2,3)


def first_function(a):
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

def unrelate_function(a, b, c):
    print 'among other things'
    (x for x in xrange(1000))
    for z in range(123):
        a = b*2+3
        print 'hello hello hello hello'
        unrelate_function(1,2,3)
    print 'this should not be copied from above'

b = 2
for i in xrange(1000):
  first_function(i)
