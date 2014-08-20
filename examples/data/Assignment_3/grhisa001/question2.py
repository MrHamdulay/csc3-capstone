height = eval(input('Enter the height of the triangle:\n'))
i=1
x=0
space_width=height
while i < height+1:
    space_width-=1    print(' '*space_width,'*'*i,'*'*x,sep='')    i+=1    x+=1