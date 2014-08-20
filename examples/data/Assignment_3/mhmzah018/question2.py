height=eval(input("Enter the height of the triangle:\n"))
line=1
space=height-1

for i in range(height):
   
    print(" "*space,"*"*line,sep="")
    line=line+2
    space-=1
    
    
    
    