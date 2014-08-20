mssg=input("Enter a message:\n")

def rep_pairs(s):

    if len(s)<2:
        return 0

    elif s[0]==s[1]:
        return 1 + rep_pairs(s[2::])

    else:
        return rep_pairs(s[1::])
x=rep_pairs(mssg)
print("Number of pairs:",x)
