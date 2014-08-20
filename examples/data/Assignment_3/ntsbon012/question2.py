#Bongiwe Ntshangase
#Question 2 _ASSIGNMENT 3

def tri():
    a=eval(input("Enter the height of the triangle:\n"))
    for i in range(0,a):
        print(" "*(a-i-1),end="")
        print((2*i+1)*"*")

tri()