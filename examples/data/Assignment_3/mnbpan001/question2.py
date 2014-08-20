x=eval(input('Enter the height of the triangle:\n'))
y=str(x*2)+"}"
s="{0:^"+y
for i in range(0,x):
    z='*'*(2*i+1)
    print(s.format(z))

