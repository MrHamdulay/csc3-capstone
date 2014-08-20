"""Cherise Dube
06 May 2014
Program to count the number of pairs of a character in string"""


s=input("Enter a message:\n")

def pairs(s):
    """finds the number of pairs of characters in a string"""
    
    if len(s)>2:
        if s[0]==s[1]:
            return "-"+str(pairs(s[2:]))    #The '-' will serve as a count of the number of pairs. So as a pair is taken away it is replaced by a dash.
        else:
            return str(pairs(s[1:]))
    if len(s)==2:
        if s[0]==s[1]:
            return "-"+""
        else:
            return""
x=pairs(s)
count=x.count("-")

print("Number of pairs:",count)

    
 