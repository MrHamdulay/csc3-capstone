m=eval(input("Enter the height of the triangle:\n"))
def s(m,n):
    for i in range(m):
        print(' '*(m-i-1),n*(2*i+1),sep='')
s(m,'*')