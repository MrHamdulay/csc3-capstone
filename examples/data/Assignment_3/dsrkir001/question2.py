def tri(i,t=0):
    if i == 0:
        return 0
    else:
        x = i-1
        print(' ' *(i-1) + '*' * ( t * 2 + 1 ))
        return tri( i - 1, t + 1 )
x = eval(input("Enter the height of the triangle:\n"))
tri(x)