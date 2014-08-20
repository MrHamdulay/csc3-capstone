""" Program that counts the number of repeated chars in a string
 Author: Julius Stopf0rth (STPJUL004)
 Date: 2014-05-05 """

msg = input("Enter a message:\n")

def count_pairs(astring):
    #(A) Terminating steps. if there are only 2 chars or less
    if len(astring) == 2:
        
        # Check if there is a pair
        if astring[0] == astring[1]:
            return 1 #If a pair is found
        else: 
            return 0 # If no pair is found
        
    #(B) Terminating steps. If the length is less than 2 return 0 (there cannot be a pair of 1)
    elif len(astring) < 2:
        return 0
    
    # If the string is longer than 2
    elif len(astring) > 2:
        
        # Check if the characters next to one another are the same
        if astring[0] == astring[1]:
            #(I) Recursive step. Count 1 and negate the overlap in characters
            return count_pairs(astring[:2]) + count_pairs(astring[2:])
        # Otherwise, move on
        else:
            #(II) Recursive step. Exclude the first character and check again
            return count_pairs(astring[1:])
            

# Produce output
print("Number of pairs:", count_pairs(msg))