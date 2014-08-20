# Program to count the number of pairs of repeated characters in a string
# Wongwa Giqwa
# 06 May 2014

s = input("Enter a message:\n")

def pairs(s):
    
    if s == "":
        return 0
    elif (len(s)==1):
        return 0
    
    else:
        if s[0] == s[1]:
            s = s[2:]
            return 1 + pairs(s)
        else:
            return pairs(s[1:])
        
print_string = pairs(s)
print("Number of pairs: " + str(print_string))
