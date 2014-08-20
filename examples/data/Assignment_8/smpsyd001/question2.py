#6 May 2014
#Pairs
#Sydney Simpson

def pairs(string):
    if len(string)<2:
        return 0
    else:
        if string[0]==string[1]:
            return 1+ pairs(string[2:])
        else:
            return pairs(string[2:])
string=input("Enter a message:\n")
print("Number of pairs:", pairs(string))