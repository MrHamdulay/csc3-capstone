import math 
x=0
funcs=input("Enter a function f(x):"'\n')
#func=x+2
#func==False
#ask tutor how to get input value 
for y in range (10,-11,-1):
      for x in range (-10, 11):
            func=eval(funcs)
     #       while func<0:
#                  func=input("hey") #finding function?
            
            
#                  func = input("what")
      #drawing the graph
          #  func=x+2
         #   func=a
            y_real = -y/10
            if x == 0 and y == round(func):
                  print ("o",end="")
            elif y == 0 and y == round(func):
                  print("o", end="")  
                   
            elif round(func) == y:
                  print("o",end="")
            
            elif x==0 and y==0:
                  print("+", end="")
            elif x==0:
                  print("|",end="")
           #getting the axis
            elif y==0:
                  print("-", end="")
            else:
                  print (" ",end="")   
      print ()
     