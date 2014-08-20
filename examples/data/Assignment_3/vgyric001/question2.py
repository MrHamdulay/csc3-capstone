height = eval(input("Enter the height of the triangle: \n"))

for i in range(1,height*2,2):
    height = height - 1
    print(" "*height+'*'*i)

   