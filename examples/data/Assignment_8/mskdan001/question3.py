"""danson masuka
 recursive function to encrypt a message by converting all lowercase characters to the next character
 5 may 2014"""

def encrypt(message):
    if len(message)== 1:
        #check for one character string and convert
        if message[0] == 'z':
            return 'a'
        return chr(ord(message)+1)
    elif message[0] == " ":
        return " "+encrypt(message[1:])
    elif message[0] == '.':
        return "."+encrypt(message[1:])
    elif message.isupper():
        return message
    #now convert to encrypted string
    elif message[0] != "z" and message[0] != ".":
        return chr(ord(message[0])+1)+encrypt(message[1:])
    else:
        if message[0] == 'z':
            return "a"+encrypt(message[1:])

message = input("Enter a message:\n")
print ("Encrypted message:")
new_message = encrypt(message)
if new_message[-1] == '/':
    print(new_message[0:len(message)-1]+".")
else:
    print (new_message)