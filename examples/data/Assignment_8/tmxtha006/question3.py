"""This function encrypt a message by shifting it 1 step up with z being shifted to a
Hebert Tema
TMXTHA006
04 May 2014"""

def encrypt(message):
    """encryption of the message 1 step up for every letter(z becomes a)"""
    if message=="": return""
    elif 122<ord(message[0]) or ord(message[0])<97:     #only lower case a-z changes
        return message[0] + encrypt(message[1:])
    elif message[0]==" ":
        return " " + encrypt(message[1:])
    elif message[0]=="z":          #avoid moving to another "set" of characters of unicode
        return "a" + encrypt(message[1:])
    else:
        return chr(ord(message[0])+1) + encrypt(message[1:])

#ger the input from the user
message=input("Enter a message:\n")

#to make the program run with both upper an lower case(del # on next line)
#message=message.lower()  

#call the encrypt function
ciphertext=encrypt(message)

#output the results
print("Encrypted message:")
print(ciphertext)