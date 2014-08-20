#Question 3
# Encrytion using recursion
#By: Dean de Haast
s = input("Enter a message:\n")

encrypted = ""

def encrypt(s):
    global encrypted
    
    if s =="":
        return (print("Encrypted message:\n",encrypted,sep=""))
    
    elif s[0] not in ("abcdefghijklmnopqrstuvwxyz"): #Checks that it is a lower case letter otherwise just leaves it
        encrypted = encrypted + s[0]
        
    elif s[0] == "z": #Checks if the letter is a "z" and then changes it to an "a"
        encrypted += "a"
        
    elif s[0]== " ":           # Carries the space down
        encrypted = encrypted + " "
        
    else:   # adds the new letter onto the other new letters
        encrypted += chr(ord(s[0])+1)
        
    return encrypt(s[1:]) # Recursive step that drops the first letter each time
encrypt(s)
