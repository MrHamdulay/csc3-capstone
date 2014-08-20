message =input("Enter a message:\n")
print("Encrypted message:")
def encrypt(message):
    if len(message)!=0:
        if message[0] == " ":
            print(" ",end='')
        elif message[0].isupper():
            print(message[0],end='')
        elif message[0] == "z":
            print("a",end='')         
        elif message[0] == ".":
            print(".",end='')
        else:
            print(chr(ord(message[0])+1),end='')
        return encrypt(message[1:len(message)])
    else:
        return True
if encrypt(message)==True:
    print(end='')
        
    