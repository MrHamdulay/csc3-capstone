height=eval(input("Enter the height of the triangle:\n"))
x=height-1
for i in range(1,height*2,2):
    print(" "*x+"*"*i)
    x-=1
    
    
