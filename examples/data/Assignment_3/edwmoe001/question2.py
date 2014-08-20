i=int(input("Enter the height of the triangle:\n"))

def asterix_triangle(i, t=0):
    if i == 0:
        return 0
    else:
        print(' ' * ( i-1 ) + '*' * ( t * 2 + 1 ))
        return asterix_triangle( i - 1, t + 1 )

asterix_triangle(i)