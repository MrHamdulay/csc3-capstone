#Ikhlaas Pohplonker
#8 May 214
#a program that counts the number of pairs of repeated characters in a string

def pairs(s):#a recursive function to count the number of pairs of repeated characters in a string
    if len(s)==1:
        return 0#adds 0
    if len(s)==2 and s[0]==s[1]:
        return 1#adds 1
    elif s[0]!=s[1]:
        return pairs(s[1:])#calls the recursive function
    else:
        return 1+pairs(s[2:])#adds one and calls the recursive function

s=input("Enter a message:\n")
print("Number of pairs:", pairs(s))