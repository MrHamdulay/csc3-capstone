"""repeated character pairs in a string
Michelle Lu
7 May 2014"""


words=input("Enter a message:\n")

def repeated_pairs(words):
    if words=="": #if it is an empty string
        return 0
    if len(words)<=1:
        return 0 #base case: last letter
    else:
        if words[0]==words[1]:
            return 1 + repeated_pairs(words[2:])
        else:
            return repeated_pairs(words[1:])
        
print("Number of pairs:", repeated_pairs(words))