def encrypt(s):
    #base case
    if s=="": #if the string has no characters, return an empty space and end.
        return ""
    #recursive step 1
    elif s[0]=="z": #if the first character of the string is z, return z and recurse the function with a slice of the string, such that the first character (the z) is removed
        return "a" + encrypt(s[1:])
    #recursive step 2
    elif not s[0].isalpha(): #if the first character is not an alphabet, return that character and recurse the function with a slice of the string, such that the first character of the that initial string is removed.
        return s[0] + encrypt(s[1:])
    #recursive step 3
    elif s[0].isupper():
        return s[0] + encrypt(s[1:]) #if the first character is in upper case, return that upper case character and recurse the function with a slice of the string, such that the first character (the upper case alphabet) is removed.
    #recursive step 4
    else:
        return chr(ord(s[0])+1) + encrypt(s[1:]) #if the first character of the string does not meet any of the above conditions, return the next character (relative to the that character the did not meet any of the above conditions), recurse the function with a slice of the string, such that the first character is removed.
    
s=input("Enter a message:\n")
print("Encrypted message:\n",encrypt(s), sep="")

    