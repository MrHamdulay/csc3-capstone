#encoding by shifting in the alphebet order
#aphiwe baleni
#9 May 2014
def encode(message):
    if message=="":
        return ""
    elif message[0]== " ":
        return " " +  encode(message[1:])
    elif message[0] != message[0].lower():
        return s[0] + encode(message[1:])
    elif message[0]=='z':
        return 'a' + encode(message[1:])
    elif message[0]== '.':
        return '.'
    else:
        x= ord(message[0])+1
        return chr(x) + encode(message[1:])
message=input("Enter a message:\n")
print("Encrypted message:\n",encode(message),sep='')