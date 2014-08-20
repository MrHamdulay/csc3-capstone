#Program to create triangles
#Tinotenda Chemvura (CHMTIN004)
#24 March 2014

h=eval(input("Enter the height of the triangle:\n"))
n=h
for i in range(1,h*2,2):
    print(" "*(n-1),"*"*i,sep="")
    n=n-1
    
    