height = eval(input("Enter the height of the triangle: \n"))

i = height-1
j = 1

for k in range(height):
    print(" "*i,"*"*j, sep=(""))
    i-=1
    j+=2
    

             
