"""count the number of pairs of repeated characters in a string
kamogelo mphela
6 may 2014"""

def check_doubles(s):
    """returns 1 if the characters next to each other are the same"""
    if len(s) <=1:
        return 0
    # accomodate the last two characters which are the same
    elif len(s) >1 and s[0]==s[1]:
        return 1 + check_doubles(s[2:])
    else:
        return check_doubles(s[1:])
    
s = input("Enter a message:\n")
check_doubles(s)

print("Number of pairs:",check_doubles(s))