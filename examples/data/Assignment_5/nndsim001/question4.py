# This program draws a text based grapgh of a mathematical function f(x)
# on a 21 x 21 grid with domain [-10,10] and range [-10,10]

# Student Name: Simeon Nandjembo

# Student Number: NNDSIM001

# 17 April 2014

import math

# Set x variable so that new local variables are not created
global x
   
   
# This function plats the graph of a user defined function   
def graph(func):
   
   for y in range (-10,11):
      for x in range (-10,11):
         
         yr = round(eval(func)) # variable to store the answer to the equation at x
         
         if (yr >= -10 and yr <=10) and yr == -y: # print equation
            print ("o",end="")
         elif x==0 and y==0: # print the origin
            print ("+",end="")
         elif x == 0: # print the y-axis
            print ("|",end="")
         elif y == 0: # print the x-axis
            print ("-",end="") 
         else: # print spaces
            print (" ",end="")   
      print ()
   
# 100,81,64,49,36,25,16,9,4,1,0,1,4,9,16,25,36,49,64,81,100
def main ():
   func = input("Enter a function f(x):\n")#func = "x**2"
   graph (func)
   #yx = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
   #for x in yx:
      #print(eval(func),",",end='',sep='')

if __name__ == "__main__":
   main ()



# Sample I/O:

# Enter a function f(x):
# x+2
#           |       o  
#           |      o   
#           |     o    
#           |    o     
#           |   o      
#           |  o       
#           | o        
#           |o         
#           o          
#          o|          
# --------o-+----------
#        o  |          
#       o   |          
#      o    |          
#     o     |          
#    o      |          
#   o       |          
#  o        |          
# o         |          
#           |          
#           |  