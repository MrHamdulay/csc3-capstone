#Draws an isosceles triangle of given height

x = eval(input("Enter the height of the triangle:\n"))
s=x-1
j=1
for i in range(0,x):
    print(s*" ", j*"*", sep="")
    j+=2
    s-=1
    
    