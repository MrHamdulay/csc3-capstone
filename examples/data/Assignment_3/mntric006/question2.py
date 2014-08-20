height = eval(input('Enter the height of the triangle:\n'))i = 1h = 0spacewidth=height
while i < height+1:    spacewidth-=1
    print(' '*spacewidth,'*'*i,'*'*h,sep='')
    i+=1
    h+=1