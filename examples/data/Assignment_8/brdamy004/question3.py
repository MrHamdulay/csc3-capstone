# Assignment 8 question 3
# Amy Brodie
# 8/05/2014


# recursion function that encrypts words
def encrypt(s,count):
    if count == len(s):
        return ""
    elif s[count] == "z":
        return chr(ord(s[count])-25) + encrypt(s,count+1)
    elif (s[count].isalpha() != True) or (s[count].islower() != True):
        return s[count] + encrypt(s,count+1)
    else:
        return chr(ord(s[count])+1) + encrypt(s,count+1)

# get input from user and output the encrypted message
message = input("Enter a message:\n")
print("Encrypted message:")
print(encrypt(message,0))