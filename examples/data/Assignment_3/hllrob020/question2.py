#triangle program
#Robin Hall
#26/03/2014

height = eval(input("Enter the height of the triangle:\n"))

symb=1 
spc=height-1

for i in range(height): 
    print(" "*spc,"*"*symb,sep ="")
    symb+=2 
    spc-=1
    