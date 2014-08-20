msg = input("Enter a message:\n")
print("Encrypted message:")
def encrypt_Msg(msg):
    if len(msg)==0:
        return True
    else:
        if msg[0] == " ":
            print(" ",end='')
        elif msg[0].isupper():
            print(msg[0],end='')
        elif msg[0] == "z":
            print("a",end='')
        elif msg[0] == ".":
            print(".",end='')
        else:               
            print(chr(ord(msg[0])+1),end='')
        return encrypt_Msg(msg[1:len(msg)])        
encrypt_Msg(msg)