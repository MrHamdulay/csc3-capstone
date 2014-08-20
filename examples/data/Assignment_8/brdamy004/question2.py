# Assignment 8 question 2
# Amy Brodie
# 8/05/2014


# recursion function to find and count all pairs of repeated characters
def pairs(s,count):
    if len(s) == 0:
        return 0
    elif count >= len(s)-1:
        return 0
    elif s[count] == s[count+1]:
        return 1 + pairs(s,count+2)
    else:
        return pairs(s,count+1)

# get input from user and output count of repeated character pairs
message = input("Enter a message:\n")
print("Number of pairs:", pairs(message,0))