#Jono Field
#May 7 
#Question 2


def Pairs(p):
    if len(p) == 1: #The base case
        return 0
    elif len(p) == 2:
        
        if p[0] == p[1]:    #compares character '1', to following character
            return 1 
        else:
            return 0
    elif p[0] == p[1]:     #process in base case is repeated
        return 1 + Pairs(p[2:])     # adds 1 to the prior value of Pairs
    else:
        return Pairs(p[1:])





Str = input("Enter a message:\n")
print("Number of pairs: "+ str(Pairs(Str)))