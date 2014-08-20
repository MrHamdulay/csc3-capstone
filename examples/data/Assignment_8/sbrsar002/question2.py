# 8 May 2014
# Sarayn Subroyen
# Program that uses a recursive function to count the number of pairs of repeated characters in a string

string = input("Enter a message:\n")

def pairs(string):
    
    if string == "":
        return 0
    elif (len(string)==1):
        return 0
    
    else:
        if string[0] == string[1]:
            string = string[2:]
            return 1 + pairs(string)
        else:
            return pairs(string[1:])
        
print_string = pairs(string)
print("Number of pairs: " + str(print_string))