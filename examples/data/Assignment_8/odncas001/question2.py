"""recursive function for identifying pairs of characters in a string
casey o'donnell
5 may 2014"""

def find_pairs(s):
    if len(s)<2:
        return 0
    elif s[0]==s[1]:
        return 1 + find_pairs(s[2:])
    else:
        return find_pairs(s[1:])
    
s=input("Enter a message:\n")
print("Number of pairs:",find_pairs(s))