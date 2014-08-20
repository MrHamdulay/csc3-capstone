'''recursive encrytption
Tim Mostert
06,05,14'''

# changes every character to ord + 1 and adds to list
# checks only for a-z and uses exeption for z
# adds other characters to list unchanged
def encrypt(message,newlist):
    
    
    if (ord(message[0])) == 122:
        newlist.append("a")
        if len(message) == 1:
            print("Encrypted message:")
            print("".join(newlist))
        else:
            encrypt(message[1:],newlist)
    elif 97 <= (ord(message[0])) < 122:
        newlist.append(chr(ord(message[0])+1))
        if len(message) == 1:
            print("Encrypted message:")
            print("".join(newlist))
        else:
            encrypt(message[1:],newlist)
    else:
        newlist.append(message[0])
        if len(message) == 1:
            print("Encrypted message:")
            print("".join(newlist))
        else:
            encrypt(message[1:],newlist)
           
message = input("Enter a message:\n")
newlist = []
encrypt(message,newlist)