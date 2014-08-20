"""
Prashanth Sridharan
SRDPRA001
Assignment 08
Question 02
"""
#Variable i is the variable name for message
#Variable j is the name for the function which defines pair counting.
def j(i):
    
    if i==i[len(i)-1]: #Step to stop recursion if the condition is met. 
        return 0 
    elif i[0]==i[1]:
        if len(i)>2:
            return 1+j(i[2:]) #recursive step
        else:
            return 1+j(i[1:]) 
    else:
        return j(i[1:])
k = input("Enter a message:\n") # variable k is the variable for inputting the message
print("Number of pairs:",str(j(k))) 
