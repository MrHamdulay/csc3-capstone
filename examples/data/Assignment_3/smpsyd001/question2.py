x=eval(input("Enter the height of the triangle:\n"))
u=x
for i in range(1,2*x,2):
    u-=1
    print(" "*(u),"*"*i,sep='')
   
    