"""A program that counts the number of pairs of repated characters in a string
Jason Findlay
08/05/2014"""

s=input("Enter a message:\n")

def pairs(s):
    #Base case
    if len(s)<2:
        return 0
    #Checks for pair
    elif s[0]==s[1]:
        return 1+pairs(s[2:])
    else:
        return pairs(s[1:])

print("Number of pairs:",pairs(s))
