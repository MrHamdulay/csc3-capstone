#Assignment 3
#Printing Triangles
#Nikhil Jiten Naik
#25 March 2014

z = eval(input("Enter the height of the triangle: \n"))
a= (z-1)*2 + 1
for i in range (1,a+2,2):
    r="{0:^{1}}".format('*'*i,z)
    print(r)

    
    