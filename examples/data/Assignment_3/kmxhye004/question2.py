height= eval(input("Enter the height of the triangle:\n"))
counter=-1
for i in range(height):
    counter=counter+2
    print(" "*(height-(i+1))+"*"*(counter))
          