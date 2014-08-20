# Program that prints an isoceles triangle of a given height using the '*' character. 
# Name: Othniel KONAN
# Student number: KNNOTH001
# Date: 20/03/2014

h=eval(input('Enter the height of the triangle:\n'))

for i in range(1,h+1):
    print(' '*(h-i),'*'*(2*i-1),sep='')
    
    