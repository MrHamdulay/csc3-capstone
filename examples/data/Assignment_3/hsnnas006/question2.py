#program to print an isoceles triangle
#by nasreen
h = eval(input("Enter the height of the triangle:\n"))
b = (h*2 - 1) #Base of triangle
indent = b//2
#prints triangle
for i in range (1, (b+1), 2): # starts indent halfway through base of triangle
    print(' '*indent, end = '')
    print('*'*i)
    indent -= 1 #decreases indent with each iteration