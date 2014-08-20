"""Assignment 8
Question 3
Micaela Menegaldo"""

def encrypt(message):
    if len(message)==1:
        if not message.isalpha():
            return message
        elif message=="z":
            return "a"
        else:
            return chr(ord(message)+1)
    elif not message[0].isalpha():
        return message[0] + encrypt(message[1:len(message)])
    else:
        if message[0]=="z":
            return "a" + encrypt(message[1:len(message)])
        else:
            return chr(ord(message[0])+1) + encrypt(message[1:len(message)])
        

if __name__=='__main__':
    message=input("Enter a message:\n")
    if message.isupper():
        emessage=message
    else:
        emessage=encrypt(message)
    print("Encrypted message:\n",emessage,sep='')