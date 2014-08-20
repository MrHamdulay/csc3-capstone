#def triangle(height,lines):
height=eval(input("Enter the height of the triangle:""\n"))
lines=height
x=(height*2)//2-1

for i in range(0,height*2,2):
   print(" "*x,end="")
   print("*"*(i+1))
   x=x-1
