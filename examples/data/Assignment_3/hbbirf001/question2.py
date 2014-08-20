h = eval(input('Enter the height of the triangle:\n'))
x=h*2
for k in range(h):
    print((('{0:^'+str(x)+'}')).format((2*(k+1)-1)*'*'))