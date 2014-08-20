# count number of repeated pairs in a string
# mllgad001
# 6 May 2014

def count_pair(s): # define function to count pairs in a string
    
    if len(s) == 0:  # base case- if length is 0 return 0
        return  0
    
    elif len(s) == 1:  # base case- if length is one return 0
        return  0
    
    elif s[0] != s[1]:         # if first 2 is not equal, calls function again, start from 2nd character
        return  count_pair(s[1:])
    
    else:
        if s[0] == s[1]:         # if first 2 is equal, calls function again
            return 1 + count_pair(s[2:])     # calls function from 3rd character so no overlapping
        
def message():    # define function to prompt user for input and calls function to count pairs
    s = input("Enter a message:\n")
    print("Number of pairs:", count_pair(s))

message()