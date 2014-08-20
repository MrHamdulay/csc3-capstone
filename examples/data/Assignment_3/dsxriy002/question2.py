#Assignment 3
#Printing Triangles
#Riya Desai
#25 March 2014

x = eval(input("Enter the height of the triangle: \n"))
y= (x-1)*2 + 1
for i in range (1,y+2,2):
    r="{0:^{1}}".format('*'*i,y)
    print(r)

    
    