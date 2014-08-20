def tri():
    size=eval(input('Enter the height of the triangle:\n'))
    height=size-1
    gap=" "
    num=1
    for i in range (size):
        print(gap*height+'*'*num)
        num+=2
        height-=1
        
tri()
        