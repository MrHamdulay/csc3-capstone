#Assignment 3 - Question 2
#Jayan Smart
#20 March 2014
x=0 #heigh
def triangle():
    x=eval(input("Enter the height of the triangle:\n"))
    y=x
    j=1
    while (j<=x):
        print(((" "*(x-j))+('*'*j))+'*'*(j-1))
        j+=1

triangle()