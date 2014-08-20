#checking for pairs
#julia breakey
#6 may 2014

#check for pairs
def pairs(word):
    if len(word)<=1:
        return 0
    elif word[0]==word[1]:
        return 1 + pairs(word[2:])
    else:
        return pairs(word[1:])

#ask for string    
string=input("Enter a message:\n")

#return pairs
print("Number of pairs:", pairs(string))