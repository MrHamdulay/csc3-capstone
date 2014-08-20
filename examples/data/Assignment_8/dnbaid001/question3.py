#Assignmnet 8 - Question 3
#Encryption using recursion
#Aidan de Nobrega
#05/05/2014

def encrypt(s):
    if s[0].isupper(): #if not lower-case, not encrypted
        if len(s) == 1:
            return s[0]
        else:
            return s[0] + str(encrypt(s[1:])) 
    elif not s[0].isalpha(): #if not a letter, not encrypted
        if len(s) == 1:
            return s[0]
        else:
            return s[0] + str(encrypt(s[1:]))
    else:
        if len(s) == 1: #base case
            x = ord(s)
            x += 1 #converts single character to next in ord
            if x > ord("z"):
                x -= 26 #z becomes a
            return chr(x) #returns new character       
        else:
            x = ord(s[0])
            x += 1
            if x > ord("z"):
                x -= 26
            x = chr(x)
            return x + str(encrypt(s[1:])) #returns new character for first letter, then moves on

def main():
    encrypted = ""
    string = input("Enter a message:\n")
    encrypted = encrypt(string)
    print("Encrypted message:\n" + encrypted)
    

main()