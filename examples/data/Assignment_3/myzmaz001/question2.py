#19 March 2014       #Mazwi Myeza
#Assignment 3        #Question2
height = eval(input("Enter the height of the triangle:\n"))
sp = height -1
b = 1
for i in range(height):
            print(" "*sp+"*"*b)
            b += 2
            sp -= 1
            
           