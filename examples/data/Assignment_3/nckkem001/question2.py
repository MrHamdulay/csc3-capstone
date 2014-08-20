y=eval(input("Enter the height of the triangle: \n"))
for i in range(1,y*2,2):
    print(('{0:^'+str(y*2)+'}').format(i*"*"))
 