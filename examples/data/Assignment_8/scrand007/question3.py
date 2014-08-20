
message = input("Enter a message:\n")

def encrypted(message):
    if message == "":
        return ""
    elif 97 > ord(message[0]):
        return message[0] + encrypted(message[1:])
    elif message[0] == 'z':
        return 'a'+encrypted(message[1:])
    elif message[0] == ' ':
        return ' '+encrypted(message[1:])
    else:
        return chr(ord(message[0])+1) + encrypted(message[1:])
    
print ("Encrypted message:\n"+encrypted(message))
    