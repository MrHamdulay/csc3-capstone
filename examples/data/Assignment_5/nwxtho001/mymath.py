'''A stupid-as module to support question3.py which asks us to do maths that isn't even covered in MAM1000W'''

def get_integer (x):
   print ('Enter ', x, ':', sep = '')
   y = input ()
   while not y.isdigit ():
      print ('Enter ', x, ':', sep = '')
      y = input ()
   y = eval (y)
   return y
   
def calc_factorial (x):
   xfactorial = 1
   for i in range (1, x+1):
      xfactorial *= i
   return xfactorial
   
if __name__ == '__main__':
   q = get_integer ('q')
   print (q)
   qfactorial = calc_factorial (q)
   print (qfactorial)