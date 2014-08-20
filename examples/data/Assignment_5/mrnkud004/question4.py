"""drawing a graph
kennedy muranda
16/4/2014"""


import math

#prompt user to enter function
function = input("Enter a function f(x):\n")

#create y-axis and x-axis
for i in range(10,-11,-1):
      
      for j in range(-10,11):
            
            x = j #convert x input by user inter a value
            y = round(eval(function))
            
            if y == i:
                  print("o",end = '')  
                  
            elif(i==0 and j==0) :
                  print('+',end = '')  
                  
            elif(i == 0):
                  print("-",end = '') 
                  
            elif(j==0):
                  print('|',end = '')
            
            else:
                  print(' ',end='')
             
             
      print()