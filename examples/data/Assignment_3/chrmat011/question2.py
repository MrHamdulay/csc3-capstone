a=eval(input("Enter the height of the triangle:\n"))

for i in range(a):
    print(' '*(a-i-1),'*'*(2*i+1),sep='')
