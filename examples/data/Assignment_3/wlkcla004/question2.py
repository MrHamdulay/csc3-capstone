h=input("Enter the height of the triangle: \n")
h2=int(h)
for i in range(1,h2+1):
    if  i ==h2:
        print('*'*(2*i-1))
    else:
        g=h2-1-i
        print(' '* g, '*'*(2*i-1))