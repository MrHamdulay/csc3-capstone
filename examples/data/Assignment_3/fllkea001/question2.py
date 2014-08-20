#Assignment 3
#Question 2
#Keanon Fell
#March 2014

a="*"
s=" "
p=1
h= eval(input("Enter the height of the triangle:\n"))

for i in range(h,0,-1):
    print((i-1)*s,a*p,sep="")
    p+=2    