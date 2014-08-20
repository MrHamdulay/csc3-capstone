"""encrypt a message using recursion
Lauren Denny
8 May 2014"""

def encrypt(string):
    if string=="": #if string is empty string,return the empty string
        return ""
    else:
        if string[0].islower() and string[0].isalpha(): #if first character in string is a lowercase alphabtic character, set "new" as the character moved 1 place down the alphabet or "z" looped back to "a"
            if string[0]=="z":
                new="a"
            else:
                new=chr(ord(string[0])+1)
        else:                                           #set new as unchanged character
            new=string[0]
        return new + encrypt(string[1:])                #return new encrypted character + the rest f the string encrypted in the same way
    
s=input("Enter a message:\n")
print("Encrypted message:\n", encrypt(s),sep="")