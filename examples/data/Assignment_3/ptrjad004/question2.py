#Jade Petersen
#Assignment 3_question 2
#28 March 2014


def triangle():
    h = eval(input("Enter the height of the triangle:\n"))
    
    for i in range (1,h+1):
        a = h - i
        print(a*" ", "*" * i, "*" * (i - 1), sep="")

triangle()