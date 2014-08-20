#Assignment 8
#Question 3

def encrypted(message):
    punctuation= [".","?","!"," "]
    if message.islower():
        if len(message) == 0:
            print(message)
        else:
            if message[0] in punctuation :
                print(message[0], end = "")
                encrypted(message[1:])
            elif message[0] == "z":
                print("a", end = "" )
                encrypted(message[1:])
            else:
                print(chr(ord(message[0]) + 1), end = "")
                encrypted(message[1:])
            
    else:
        print(message)
            
message = input("Enter a message:\n")
print("Encrypted message:")
encrypted(message)