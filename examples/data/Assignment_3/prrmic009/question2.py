# program to print an isosceles triangle of input height
# Mick Perring
# 27 arch 2014

x = eval(input("Enter the height of the triangle:""\n")) # Allows user to input triangle height

def tri (height, char):                 # Function of triangle, prints triangle of input height
        gap = height-1
        for i in range (0, 2*height, 2):
                height = (height*2)
                print (gap*" ", char*(i+1), sep="")
                gap = gap-1
                
tri(x, "*")
        