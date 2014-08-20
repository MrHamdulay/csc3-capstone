'''program to draw the graph of any function
Wandile Khowa
16-04-2014
'''

import math #I am going to use the math library
      
def my_function():
   """draws a graph of any function"""
   k = ''
   function = input("Enter a function f(x): \n")
   if function.lower()[0] == 's': #searches for 's' in a string for a special case sine function
      k = 'math.'
   else:
      k = k
   if function[0:2] == 'sin':
      new_function = 'math.'+function #add the prefix 'math.' in the string in order to call the math library for sine
   elif str(function) == str(function)[::-1]:
      y_out = function
   else:
      new_f = function
   for y in range (10, -11, -1): #amplitude of function
      for x in range (-10, 11): #runs through the domain of f(x)
         new_f = list(function)
         for i in range(len(new_f)): #it runs throughout the list to check for the letter 'x'
            if new_f[i] == 'x':
               new_f[i] = '('+str(x)+')' #replaces x with string x and a number from the ineer for loop as the input
               s = "".join(new_f) #joins the list into a string
               y_out = round(eval(k+s)) #computes the value of y
         if x==0 and y==0 and y_out != 0:
            print ("+",end="") #this tells python to print '+' when x=0 and y=0
         elif x == 0 and y_out != y and not(round(eval("".join(new_f))) == y)  :
            print ("|",end="") #this tells python to print '|' when only x = 0 and ontop of each other >>end=''<< +++y-axis+++
         elif y == 0 and y_out != 0:
            print ("-",end="") #this tells python to print '-' when y=0 >>>x-axis
         elif y == y_out:
            print ("o",end="")
         elif y == 0 and y_out == 0: #tells python to print 'o' if y_out is an x & y intercept
            print ("o",end="")
         elif (y == y_out or y == round(eval("".join(new_f)))) :
            print("o", end="")
         else:
            print (" ",end="")   #tells python to continue if there is no value in that block
      print ()
      
my_function()

      

      
                