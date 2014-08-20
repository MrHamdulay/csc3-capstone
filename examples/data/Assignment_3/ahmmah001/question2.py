#Mahnoor Ahmed
#AHMMAH001
#Drawing isoceles triangles

x=eval(input("Enter the height of the triangle:\n"))
y=1
for i in range(x):
    space=" "*(x-1)
    x=x-1
    chr="*"*(y)
    y=y+2
    print(space,chr,sep="")