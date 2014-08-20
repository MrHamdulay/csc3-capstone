# Mikhaila Sorour
# 25 March 2014
# Program to draw an isoceles triangle of given height

height = eval(input("Enter the height of the triangle:\n"))

gap=height  
for i in range(0,height*2,2):
          print(' '*(gap-1),end='')  
          print('*'*(i+1))
          gap-=1 

