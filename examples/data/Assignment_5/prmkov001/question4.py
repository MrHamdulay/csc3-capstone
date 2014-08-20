#Kovlin Perumal
import math

function = input("Enter a function f(x):\n")

for i in range(10,-11,-1): # Define for loop for the y axis
      
      for j in range(-10,11): # Define for loop for the x axis
            
            x = j
            y = round(eval(function)) #Evaluate inputted function
            
            if y == i:
                  print("o",end = '')  #If the y value is equal to the value on the plane of the graph print 'o'
                  
            elif(i==0 and j==0) :
                  print('+',end = '')  
                  
            elif(i == 0):
                  print("-",end = '') 
                  
            elif(j==0):
                  print('|',end = '')
            
            else:
                  print(' ',end='')
             
             
      print() #Move cursor to next line