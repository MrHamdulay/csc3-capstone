#Shahrain Coovadia
#CVDSHA002

x=eval(input("Enter the height of the triangle:\n"))

y=1
for i in range (0,x):
    x+=-1
    print(" "*(x),'*'*y,''*x, sep="")
    y+=2
    