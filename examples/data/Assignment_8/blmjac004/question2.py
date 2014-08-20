"""checking to see how many pairs of letters there are in a string
Jacqueline Blomendahl
8 may 2014"""

s = input("Enter a message:\n")
counter=0

def double_check(s):  #defining function
    
    if len(s)<2:
        return counter
        
    if s[0]==s[1]: #checking for same leter
        return 1+ double_check(s[2:])
        
    else:             
        return double_check(s[1:]) #using recursion for the next letter
    

    
print("Number of pairs:", double_check(s))
double_check(s)