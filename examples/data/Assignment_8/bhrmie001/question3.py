# Miengha Behardien
# Assignment 8
# 4 May 2014

def encrypt(string):                #encrypts given string
    new_letter=ord(string[0])+1                  #adds one to the unicode of a letter
    if len(string)<=1:
        if (ord(string[0])<97):
            return string[0]
        if string[0]=="z":
            return "a"
        else:
            return chr(new_letter)
    if string[0]=="z":
                return "a" + encrypt (string[1::])    
    if (ord(string[0])<97):
            return string[0] + encrypt(string[1::])    
    if string[0]==".":
        return "." + encrypt(string[1::])
    if string[0]==" ":
        return " " + encrypt (string[1::])
    else:
        return chr(new_letter) + encrypt(string[1::])       #returns encoded string

def main():
    string=input("Enter a message:\n")
    string=encrypt (string)
    print("Encrypted message:\n", string, sep="")

main()