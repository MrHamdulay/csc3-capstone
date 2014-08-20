#glnrus002
#Question 4
#16 april
import math

def actual():
   function=input("Enter a function f(x):\n")
   for y in range (-10,11):#range
      for x in range (-10,11):#domain
         function.replace("x","("+str(x)+")")#replace x with number in domain
         ans=round((eval(function))*-1) 
         
         if ans==y:
            print("o",end="")
         
         elif x==0 and y==0:#print origin
            print("+",end="")
         

         elif y==0: #print x axis
            print("-",end="")
         
         elif x==0:#print y axis
            print("|",end="")

         else:# adds spaces for shape
            print(" ",end="")
      print()


if __name__=="__main__":
   actual()
    
