"""count number of pairs
Paul Truter
06 May 2014"""

s= input("Enter a message:\n")

def pairs(s):
    if len(s) <= 1:
        return 0
    elif len(s) >= 2:
        if s[0] == s[1]:
            return 1 + pairs(s[2:])
        else:
            return pairs(s[1:])

print("Number of pairs:",pairs(s))