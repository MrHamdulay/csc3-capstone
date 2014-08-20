""" program that uses a recursive function to encrypt a message by converting
all lowercase characters to the next character (with z transformed to a). 
Dylan Feldner-Busztin
08 May 2014"""

message = input("Enter a message:\n")
newmessage = ""
reps = len(message)
print("Encrypted message:")


def encrypt(message,newmessage,reps):
    
    if reps == 0:
        
        print(newmessage)
        
    else:
        
        if message[0] == " ":       
            newword = " "                
        
        elif not 97 <= ord(message[0]) <= 122:
            newword = message[0]
             
        elif message[0] == "z":
            newnum = ord(message[0]) - 25       
            newword = chr(newnum)            
    
        else:    
            newnum = ord(message[0]) + 1       
            newword = chr(newnum)
        
        newmessage = newmessage + newword
        
        reps -= 1
        encrypt(message[1:],newmessage,reps)
        
encrypt(message,newmessage,reps)