def pyramid(rows=8):
    for i in range(rows):
        print (' '*(rows-i-1) + '*'*(2*i+1))

n=eval(input("Enter the height of the triangle:\n"))
pyramid(n)