"""a program that uses a recursive function to encrypt a message by converting all lowercase characters to the next character
fadzai mupfunya
08 may 2014"""


message=input("Enter a message:\n")

def replace(s):
    #the base case 
    if s == "":
        return ""
    else:
        first_character = s[0]    #for the first position
        if first_character.islower() and first_character.isalpha():      #to make sure the character is a letter and is in lowercase
            if first_character == "z": #to swap z with a
                return "a" + replace(s[1:])
            else:
                first_character=chr(ord(first_character)+1) #to change the first letter to the next letter
        return (first_character + replace(s[1:])) #to return the character that you have changed to the rest of the string

print("Encrypted message:")
print(replace(message))
