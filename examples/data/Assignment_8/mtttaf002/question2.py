"""count the number of pairs of repeated characters in a string
tafara mtutu
06 may 2014"""

def pairs_in(words):
    if len(words) < 2:
        return 0
    else:
        if words[0] == words[1]:
            return 1 + pairs_in(words[2:])
        else: return pairs_in(words[1:])
        
x = input("Enter a message:\n")
if x:
    print("Number of pairs:", pairs_in(x))
