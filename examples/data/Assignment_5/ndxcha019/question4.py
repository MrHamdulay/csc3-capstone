'''Luke Naude
program to graph functions
14 April'''

import math

f_of_x=input('Enter a function f(x):\n')
'''make the graph'''
for y in range (10,-11,-1):
                  if y!=10:
                                    print('')
                  for x in range (-10,11):
                                    f_evaled=round(eval(f_of_x))
                                    if y==f_evaled:
                                                      print('o',end='')
                                    elif x==0 and y==0:
                                                      print('+',end ='')
                                    elif x==0:
                                                      print('|',end='')
                                    elif y==0:
                                                      print('-',end='')
                                    else:
                                                      print(' ',end='')