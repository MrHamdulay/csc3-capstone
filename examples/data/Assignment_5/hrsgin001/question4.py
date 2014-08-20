import math
func = input("Enter a function f(x):\n")


for y in range(10, -11, -1):
   for x in range(-10, 11):
      
      if (func.find("x**") != -1): 
         pos = func.find("x**") + 3
         if(eval(func[pos])%2 == 0):#if x is to the power of an even num
            stx = str(abs(x))
         else:
            stx = str(x)
      else:
         stx = str(x)
      yvalue = round(eval(func.replace("x", stx)))
      if y == yvalue:
         print ("o",end="")
      elif x==0 and y==0:
         print ("+",end="")
      elif x == 0:
         print ("|",end="")
      elif y == 0:
         print ("-",end="")
      else:
         print (" ",end="")   
   print("")
