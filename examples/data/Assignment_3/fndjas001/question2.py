#A program that prints an isoceles triangle of a given height
#Jason Findlay
#28/03/2014

i=0
height=eval(input('Enter the height of the triangle:\n'))

while i<height-1:
    print(' '*(height-2-i),'*'+'*'*(i*2),' '*(height-1-i))
    i+=1
    
if height!=0:
    print('*'+'*'*(i*2))
