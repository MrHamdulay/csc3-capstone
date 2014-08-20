import math
yinc=1/20
def graph2(s):
   for y in range(-10,11):
        
      for x in range(-10,11):
         
         if s.find("**") == True or s.find("**")==0:
            if x<0:
               x=-x   
         k="("+str(x)+")"
         f=s.replace("x", k)
        
         f=eval(f)
            
         x_real=f/10
         y_real=-y/10
         if y_real-yinc<=x_real<=y_real+yinc:
            print("o", end="")
         elif x==0 and y==0:
            print("+",end="")
         elif x==0:
            print("|", end="")
         elif y==0:
            print("-", end="")           
         else:
            print(" ", end="")
      print()
      
            

   
if __name__ == "__main__":
      
      f_x=input("Enter a function f(x):\n")
      y=str(f_x)
      graph2(y)
   