#Encrypt
#Sofia Palmer
#4 May 2014

message = input("Enter a message: \n")
print("Encrypted message:")

def encrypt(position, message):
    if (position < len(message)):
        #check for uppercase
        if (message == message.upper()):
            return print(message)
        #changes made for punctuation and z
        if (message[position] == "z"):
            print("a", end="")            
        elif (message[position] == "."):
            print(".", end="")         
        elif (message[position] == " "):
            print(" ", end="")     
        else:
            #increase letter by 1
            char = chr(ord(message[position]) + 1)
            print(char, end="")
        return encrypt(position+1, message)
    else:
        return

encrypt(0, message)
    
    