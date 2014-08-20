"""Assignment 8- Question 1
Duncan Saffy
4 May 2014"""
def pal(x):
    if x[0]==x or x[0:2]==x:
        return 1
    
    elif x[0]==x[-1]:
        return pal(x[1:(len(x)-1)])
    
    else:
        return 0
    
x=input("Enter a string:\n")
if pal(x)==0:
    print("Not a palindrome!")
    
else:
    print("Palindrome!")