""" Bella Gorham 
graph drawing
14/04/2014"""



import math
   

def draw_graph ():
   #get input
   z = input("Enter a function f(x):\n")
   
   #make grid
   for y in range (-10,11):
      for x in range (-10, 11):
         
         #get values
         x_real = round(eval(z))
         y_real = -y
         
         #draw graph points
         if x_real==0 and y_real==0:
            # for intercepts
            print ("o",end="")
         
         elif y_real == x_real :
            print ("o",end="")  
            
         #draw middle point
         elif x ==0 and y == 0:
            print("+",end="")
            
      #draw aaxis
         elif x == 0:
            print ("|",end="")
            #axis
         elif y == 0:
            print ("-",end="")
            #axis
        
            #points on graph
         else:
            print (" ",end="")   
            #spaces
      print ()
   
def main ():
   draw_graph ()

if __name__ == "__main__":
   main ()

