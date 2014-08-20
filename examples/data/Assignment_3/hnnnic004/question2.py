height=eval(input("Enter the height of the triangle:\n"))

gap=height-1
for i in range(0,height,1):
       print(' '*gap,end='')
       print("*"*(1+2*i))
       gap=gap-1