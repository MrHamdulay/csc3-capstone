h=eval(input('Enter the height of the triangle:\n'))
gap =  h//2
for i in range(h):
    if h%2==0:print(' '*((gap*2-1)-i)+'*'*(2*i+1))
    else:print(' '*((gap*2)-i)+'*'*(2*i+1))