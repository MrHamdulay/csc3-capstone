height = eval(input("Enter the height of the triangle: \n"))
space = height-1
for i in range(1,height+1):
    
    i = (i*2)-1
    print((" "*space)+(i*"*"))
    space = space -1
    