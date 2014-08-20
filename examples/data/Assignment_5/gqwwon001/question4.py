import math

# Function to calculate y-values
def y_values(x,formula):
   y_output = round(eval(formula.replace('x','('+str(x)+')')))
   # To correct the graph
   y_output*=-1
   return y_output

# Function to compute and to draw the graph
def draw_graph():
   formula = input('Enter a function f(x):\n')
   y_inc = 1//10
   formula=formula
   
   for y in range(-10,11):
      for x in range(-10,11):
         if x==0 and y==0:
         # Search for where the conditions are satisfied in the axes, taking intercept into account
            if y-y_inc <= y_values(x,formula) <= y+y_inc ==0:
               print('o',end='')
            else:
               print('+',end='')
         elif x==0:
            if y-y_inc <= y_values(x,formula) <= y+y_inc ==y and x == 0:
               print('o',end='')
            else:
               print('|',end='')
         elif y==0:
            if y-y_inc <= y_values(x,formula) <= y+y_inc == 0:
               print('o',end='')
            else:
               print('-',end='')
         elif y-y_inc <= y_values(x,formula) <= y+y_inc:
            print('o',end='')
         else:
            print(' ',end='')
      print()    
draw_graph() 
    