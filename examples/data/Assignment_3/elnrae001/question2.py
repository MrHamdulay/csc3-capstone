# Author: Raees Eland
# Question 2: printing a triangle given the inputed height.
# 25 March 2014

x=eval(input('Enter the height of the triangle:\n'))
gap=((x*2)//2)-1
for i in range(0,(x*2),2):
   print(' '*gap,end='')
   print('*'*(i+1))
   gap-=1
   