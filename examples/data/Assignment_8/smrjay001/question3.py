"""
Assignment 8 - Question 3
Program to encript a message
Jayan Smart
7 May 2014
"""

def encrypt(s):
    if s == "":
        return s
    else:
        if 97<=ord(s[0])<=122:
            if (ord(s[0])) == 122:                    #If z, convert to a
                return  "a"+encrypt(s[1:])
            else:                                   #Replace each charactor with the next one in alphabet
                return chr(ord(s[0])+1)+encrypt(s[1:])
        else:
            return s[0] + encrypt(s[1:])
def main():
    
    text = input("Enter a message:\n")
    print("Encrypted message:\n"+encrypt(text))

if __name__ == "__main__":
    main()
