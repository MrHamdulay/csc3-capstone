__author__ = 'George'
height = eval(input("Enter the height of the triangle:\n"))
space = height
num = 1
for a in range(1,height+1):
    space -= 1
    print(" "*space,"*"*num,sep="")
    num += 2