'''Program that uses recursion to count the amount of pairs in a string
Frans van Hoek
8 May 2014'''



def pairs(s):
    if len(s) < 2:
        return 0
    elif s[0]==s[1]:
        return 1 + pairs(s[2:])
    else:
        return 0 + pairs(s[1:])

ans = input("Enter a message:\n")
print ("Number of pairs:", pairs(ans))