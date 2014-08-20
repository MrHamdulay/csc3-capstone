"""pair counter
clare walker
5 may 2014"""

def pairs(string):
    if len(string) ==1: # if only one left because last two were a pair, add 0 
        return 0
    if len(string) ==2: #if last two, only return 1 if they are equal
        if  string[0] ==string[1]:
            return 1
        else:
            return 0
    elif string[0] ==string[1]: #find equal, add 1
        return 1 + pairs(string[2:])
    else:
        return 0 + pairs(string[1:]) #find not equal, add 0
 # use functions with input   
message=input("Enter a message:\n")
print("Number of pairs:", pairs(message))