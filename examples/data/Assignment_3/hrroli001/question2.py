# Question 2 - Assignment 3
# Oliver Harrison HRROLI001
# 21 March 2014

h=input("Enter the height of the triangle: \n")
i=1
h=eval(h)
while i<=h:
        print((((((h*2)-1)-((i*2)-1))//2))*" ",((i*2)-1)*"*",(((((h*2)-1)-((i*2)-1))//2))*" ",sep="")
        i=i+1