"""Lowercase Encrypter"""
#Liam Brodie
#BRDLIA004
#May 2014

print("Enter a message:")
msg = input("")


newmsg = ""

def crypt(msg):
    if msg == "":                   #Check if string is empty
        print("Encrypted message:")
        global newmsg
        print(newmsg)
    if msg[0] == msg[0].lower():  #Check if character is in lowerecase
        if msg[0] == " ":
            newmsg += msg[0]
            return crypt(msg[1:])
        if msg[0] == ".":        #Check if character is a fullstop
            newmsg += msg[0]
            print("Encrypted message:")
            print(newmsg)            
        
        if msg[0] == "z":       #Check if character is a "z"
            add2msg = "a"
            newmsg += add2msg
            if len(msg) > 1:
                return crypt(msg[1:])
            elif len(msg) == 1:
                print("Encrypted message:")
                print(newmsg)
        
        elif msg[0] != " " and msg[0] != "z" and msg[0] != ".": #Check if character is a letter.
            add2msg = chr(ord(msg[0])+1)
            newmsg += add2msg
            if len(msg) > 1:
                return crypt(msg[1:])
            elif len(msg) == 1:
                print("Encrypted message:")
                print(newmsg)
    else:                   #Check if character is an uppercase letter
        newmsg += msg[0]
        if len(msg) > 1:
            return crypt(msg[1:])
        elif len(msg) == 1:
            print("Encrypted message:")
            print(newmsg)        
    
crypt(msg)