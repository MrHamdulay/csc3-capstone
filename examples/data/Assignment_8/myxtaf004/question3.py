"""Encrypts a message
Tafadzwa Moyo
4 May 2014"""

#encryptes message
def encrypt(msg):
    alph="abcdefghijklmnopqrstuvwxyz"
    if len(msg): #Checks if msg is not blank
        
        if alph.find(msg[0])==alph.find("z"): #checks if the character is "z"
            a="a"
        elif not msg[0] in alph : #checks for special characters
            a=msg[0]
        else:
            a=alph[alph.find(msg[0])+1]
        return a+encrypt(msg[1:]) #returns encrypted message
    else: return ''

#input
msg=input("Enter a message:\n")
print("Encrypted message:\n", encrypt(msg), sep='')