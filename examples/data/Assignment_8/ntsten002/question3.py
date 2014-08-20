message = input("Enter a message:\n")
capitals = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def encrypt(message):
    if message =="":
        return message
    if message[0].isalpha() == False:
        return message[0]+encrypt(message[1:])
    elif message[0] in capitals:
        return message[0]+encrypt(message[1:])
    else:
        x = ord(message[0])
        x+=1
        if x> ord("z"):
            x-=26
        return chr(x)+encrypt(message[1:])
    

print("Encrypted message:\n"+encrypt(message))