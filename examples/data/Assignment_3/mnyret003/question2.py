rows = eval(input("Enter the height of the triangle:\n"))
for i in range (rows):
    print( ' '*(rows-i-1) + '*'*(2*i+1))