import math
def fx():
   exp=(input("Enter a function f(x): \n"))#("x+2")
   for y in range(10,-11,-1):  #to iterate between 10 to 20 bacwards
      
      for x in range(-10,11): #to iterate on the factors of the number
         
         y_value=eval(exp.replace("x","("+str(x)+")")) #we need to replace the x from the user into the string of x we are going to use to calculate< after that has happend we evaluate it to become a number
         
         
         y_inc=0.5 #this is to make sure that when y meets x and may not be in the center of each graph incriment it will still be veiwed due to the range of 0.5
         if y_value-y_inc<=y<=y_value+y_inc:
            
            print ("o",end="") #this is meant to diplay the graph if the condition of y=exp is met
         elif x==0 and y==0:
            print ("+",end="") #this is used to make the orgin of the graph a + point 
         elif x==0:
            print ("|",end="") #this is used to make the y axis line by printing "|" after the other in a vertical line
         elif y==0:
            print ("-",end="") #this is used to make the x axis by printing "-" in a horizontal line
         else:
            print (" ",end="") #this is used to print emptyness throughout our whole range of y in range(10,-10, and x in range(-10,10
   
      print () #this indicates the python language to now start on a new line after all conditions have been met    
   #else:                  # else part of the loop
    #  print num, 'is a prime number'
fx() #lets call the function now