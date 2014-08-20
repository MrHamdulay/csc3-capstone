#Sandisha Budhal
#BDHSAN003

# a function to count the number of pairs
def pairs (strngs):
    if len(strngs)==1:
        return 0
    elif len(strngs)==2:
        if strngs[0]==strngs[1]:
            return 1
        else:
            return 0
    elif strngs[0] == strngs[1]:
        return 1 +pairs(strngs[2:])
    else:
        return 0 +pairs(strngs[1:])

strngs=input("Enter a message:\n")
print("Number of pairs:", pairs(strngs))

 
        
 
        
   

