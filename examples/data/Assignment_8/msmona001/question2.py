"""recursive function calculating pairs of repeated characters
Onalerona Mosimege
04 May 2014"""

def PairsCount(s):
    """counts the number of pairs of repeated characters in a string"""
    #Base Case
    if s == "":
        return 0

    #First recursive statement- compare two letters only if length of string is 2 or more
    elif len(s) >=2:
        if s[0] == s[1]:
    
            return 1 + PairsCount(s[2:])
    #Second recursive statment - if only one letter, return
    else:
        return PairsCount(s[1:])

    return PairsCount(s[1:])
    
   
s= input('Enter a message:\n')
count = PairsCount(s)
print("Number of pairs:",count)