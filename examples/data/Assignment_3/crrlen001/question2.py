par1 = eval(input("Enter the height of the triangle:\n") )
par2 = '*'

gap=(par1+par1-1)//2
for i in range(0,par1+par1-1,2):
        print(' '*gap, end='')
        print(par2*(i+1))
        gap=gap-1
 
#Author: Lenard Carroll
#Student Number: CRRLEN001