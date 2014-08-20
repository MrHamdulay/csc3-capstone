#assignment 8 Q3 - encryption
#Kavr Ranchod RNCKAV001
#05/05/2014

#Acquire input
message = input("Enter a message:\n")
#Initialize counter and empty string
x = 0
new = []
def encrypt (message):
    global x
    global new
    #End recursion after all characters have been analysed
    if x < len(message):
        #Find the unicode value of the character
        unicode = ord(message[x])
        #If character is not lowercase
        if unicode < 97 or unicode > 122:
            new.append(chr(unicode))
            x += 1
            return encrypt(message)
        #If character is z
        elif unicode == 122:
            new.append("a")
            x += 1
            return (encrypt(message))
        #If character is lowercase
        elif unicode in range(97,122):
            newch = chr(unicode + 1)
            new.append(newch)
            x += 1
            return encrypt(message)
    #Join individual strings
    else:
        new = "".join(new)
        print("Encrypted message:\n", new, sep="")
encrypt(message)