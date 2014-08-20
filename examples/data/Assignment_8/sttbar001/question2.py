"""count the number of pairs of repeated characters in a string
barak setton
04/05/2014"""

def count(n):
    if n=="":
        return 0
    elif len(n)==1: #  telling when to stop
        return 0
    elif n[0]==n[1]: # checking to see is it repeated  
        return 1+count(n[2:]) # adding to counter
    else:
        return count(n[1:]) # making the issue smaller
    
s = input("Enter a message: \n")
amount = count(s)
print("Number of pairs:", amount)
