"""program to count the number of pairs of prepeated characters in a string
Kristin Kinmont
3 May 2013"""

def count(s):
    if len(s) == 1:
        return 0
    elif s[0] == s[1]:
        if len(s)>=3:
            return 1 + count(s[2:])
        else:
            return 1
            
    else:
        return count(s[1:])
s = input("Enter a message:\n")
print("Number of pairs:", count(s))