#Amitha Doodnath
#DDNAMI001
#24/03/2014
#Programme to print user defined inverse isosceles triangle

height=eval(input("Enter the height of the triangle:\n"))

for i in range(height):
    print(" "*(height-i-1),"*"*(((i+1)*2)-1),sep="")