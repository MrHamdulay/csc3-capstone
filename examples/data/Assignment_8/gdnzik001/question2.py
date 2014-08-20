"""program to count the number of pairs of repeated characters in a string
Zikho Godana
08 May 2014"""

s=input("Enter a message:\n")

def countpairs(s):
    """counts pairs of repeated characters in a string"""
    if s=="":
        return 0
    elif s[0]==s[1]:
        return countpairs(s[1:])
    else:
        return 0
    
print("Number of pairs:",countpairs(s))    