# Najeeb Sirkhoth
# SRKMOH002
# question2.py
# Assignment 8  


# Recursive funtion for checking pairs in string
def pairs(string):
    if len(string) == 1:                              # Base Case 1, when 1 literal remains
        return 0
    elif len(string) == 2:                            # Base Case, when 2 literals remain
        if string[0] == string[1]:
            return 1
        else:
            return 0
    else:                                             # Recursion step 
        if string[0] == string[1]:
            return 1 + pairs(string[2:])              # Prevent overlap of pairs
        else:
            return 0 + pairs(string[1:]) 

# Get user message        
x = input("Enter a message:\n") 
print ("Number of pairs:", pairs(x))                 # print number of pairs
