# Sohail Tulsi TLSSOH001
# 24/03/2014
# Drawing a triangle

height = eval(input('Enter the height of the triangle:\n'))
gap = height-1
for i in range(height):
    
    print(' '*(gap),'*'*((i*2)+1),sep="")
    gap-=1
    