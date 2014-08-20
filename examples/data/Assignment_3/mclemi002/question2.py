#emile mclennan
#23/3/14
#q2 A3

height = eval(input("Enter the height of the triangle:\n"))

for i in range(height):
    print(' '*(height-i-1)+'*'*(2*i+1))