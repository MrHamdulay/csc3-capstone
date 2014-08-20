H=eval(input('Enter the height of the triangle:\n'))
V=1
for i in range(H):
    print((H-1)*' ',V*'*', sep='')
    H=H-1
    V=V+2


