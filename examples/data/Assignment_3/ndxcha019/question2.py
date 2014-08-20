height = eval(input('Enter the height of the triangle:\n'))
i=1
sh=0
space_width=height
while i < height+1:
    space_width-=1
    print(' '*space_width,'*'*i,'*'*sh,sep='')
    i+=1
    sh+=1