#Assignment 3
# Question 2

height= eval(input("Enter the height of the triangle:\n"))
gap= height-1

for i in range(1,(height*2),2):
    print(gap*" ","*"*i, sep="")
    gap=gap-1