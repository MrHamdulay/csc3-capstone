"""graphing a function
danica van der zandt
15 april 2014"""


import math

function=input("Enter a function f(x):\n")

def calc(x):
#get y values for every x value     
   y=eval(function)
   return y   

def graph ():
#graph the function where a coord is represented by "o"
   #xpt=calc()
   for y in range (-10,11):
      
      for x in range (-10, 11):
         x_coord = x
         y_coord = -y
         
         if y_coord==round(calc(x)):
            print("o",end="")
            continue
            ##why is this not working?  if the y value obtained from the calc function = the graph y why wont it plot it?
         ##where do i incorporate my function calc?
         if x_coord == 0:
            if x_coord==0 and y_coord==0:
               print ("+",end="")
            elif x_coord == 0:
               print ("|",end="")
         elif y_coord == 0:
            print ("-",end="")
         else:
            print (" ",end="")      
      print ()
 
 

def main ():
   graph ()

if __name__ == "__main__":
   main ()

        
                  
    



