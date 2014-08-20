"""Amy Bosworth, Assignment 8, Question 2, 6 May"""

msg=input("Enter a message:\n")

def pairs(msg):
    
    #if no input or 1 letter(no pairs)
    if len(msg) == 1 or len(msg) == 0:
        return 0
    
    elif msg[0]==msg[1]:
        return 1 + pairs(msg[2:])
    
    else:
        return pairs(msg[1:])

print("Number of pairs:", pairs(msg))

    

