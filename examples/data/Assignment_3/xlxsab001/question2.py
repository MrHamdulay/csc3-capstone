
x=eval(input("Enter the height of the triangle:\n"))
def a(x):
     gap=(x-1)
     for i in range(0,x*2-1,2):
          print(' '*gap,end="")  
          print("*"*(i+1))
          
     
          gap=gap-1 # can also write this as: gap-=1
         
          
a(x)