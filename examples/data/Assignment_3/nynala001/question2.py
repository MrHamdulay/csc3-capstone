size = eval(input("Enter the height of the triangle:\n"))

j = size
for i in range(1,size*2,2):
    j = j -1
    print( ' ' * j + '*' * i)