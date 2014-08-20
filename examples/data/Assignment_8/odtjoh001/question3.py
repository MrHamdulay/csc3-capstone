def convert(message):
    if message.isupper():
        print(message)
    else:
        if len(message) != 0:
            if(message[0] == "z"):
                print(chr(ord(message[0])-25), end = "")
                convert(message[1:])
            elif(message[0] in " !.,/" ):
                print(message[0], end = "")
                convert(message[1:]) 
            else:
                print(chr(ord(message[0])+1), end = "")
                convert(message[1:])            
mes = input("Enter a message:\n")         
print("Encrypted message:")
convert(mes)
    