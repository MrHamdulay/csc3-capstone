# Question 4
# Richard van Gysen
# 15 April 2014

# import math

import math

# get an input function

function = input("Enter a function f(x): \n")

# graph function
for y in range (10,-11,-1):
                  if y!=10:
                                    print('')
                  for x in range (-10,11):
                                    functionv = eval(function)
                                    functionv = round(functionv)
                                    if y == functionv:
                                                      print ("o",end="")
                                    elif x==0 and y==0:
                                                      print ("+", end ='')
                                    elif x == 0:
                                                      print ("|",end="")
                                    elif y == 0:
                                                      print ("-",end="")
                                    else:
                                                      print (" ",end="")