"""program to count number of pairs of repeated chatacters in a string
joshua gullan
8 may 2014"""

def paircount(x):
    if len(x)==1:
        return 0
    elif len(x)==2:
        if x[0]==x[1]:
            return 1
        else:
            return 0
    
    elif x[0] == x[1]: #checks for repeat of letter
        return 1  + paircount(x[2:])#adds one to the count and moves onto next iteration 
    else:
        return paircount(x[1:]) #if letter is not repeated, don't add to count
    


x=input("Enter a message:\n")
print("Number of pairs:",paircount(x))

