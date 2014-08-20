# A program that uses a recursive function to count the number of pairs of repeated characters in a string. 
# Pairs of characters cannot overlap.  
# MUST NOT use any form of loop in the program!

def count(p):
    if len(p) == 1:
        return 0
    
    elif len(p) == 2:
        if p[0] == p[1]:
            return 1
        
        else:
            return 0
    
    
    elif p[0] == p[1]:
        return 1 + count(p[2:])
    
    else:
        return count(p[1:])


string = input("Enter a message:\n")

print("Number of pairs: " + str(count(string)))
