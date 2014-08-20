h=eval(input("Enter the height of the triangle:\n"))
x=h-1
gap=x
s=1
for i in range(h):               
 print(" "*gap+("*"*s)+" "*gap)
 gap-=1
 s+=2


