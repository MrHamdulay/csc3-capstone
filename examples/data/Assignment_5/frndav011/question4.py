"""Program to sketch functions
David Fransch
15-04-2014"""
import math#To use special functions e.g. math.sin(x)
fn = input("Enter a function f(x):\n")

for y in range(10,-11,-1):
   if y == 10: 
      #print()#Print new line
      for x in range(-10,11):
          #Prints x and y axis
          fn2 = eval(fn)
          y1 = round(fn2)
          
          if x==0 and y == 0:
              if y1==y:
                  print("o", end='')
              else:
                  print("+", end ='')
              
          elif y == 0:
              if y1==y:
                  print("o", end='')
              else:
                  print ("-", end='')
          elif x == 0:
              if y1==y:
                  print("o", end='')
              else:
                  print ("|", end='')
              
      
          
          #Prints function
          elif y1 == y:
              print("o", end='')
          
          else:
              print(" ",end='')
   else: 
      print()
      for x in range(-10,11):
          #Prints x and y axis
          fn2 = eval(fn)
          y1 = round(fn2)
          
          if x==0 and y == 0:
              if y1==y:
                  print("o", end='')
              else:
                  print("+", end ='')
              
          elif y == 0:
              if y1==y:
                  print("o", end='')
              else:
                  print ("-", end='')
          elif x == 0:
              if y1==y:
                  print("o", end='')
              else:
                  print ("|", end='')
              
      
          
          #Prints function
          elif y1 == y:
              print("o", end='')
          
          else:
              print(" ",end='')      
    
    
        

        
              