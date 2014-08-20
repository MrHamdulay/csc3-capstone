x=eval(input("Enter the height of the triangle:\n"))
def pyramid(x):
    for i in range(x):
        i=i+1
        r=x-i
        print(' '*r+"*"*(2*i-1))
pyramid(x)