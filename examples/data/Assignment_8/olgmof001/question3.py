
"""Tofunmi Olagoke
5 May 2014
Programme encypting a message"""

def main(message):
    
    if message.islower(): #check if lower case
    #finds the position of the following alphabet and replaces original alphabet with it
        if len(message) == 0:
            print(message)
        else:
            if message[0] in "string" :
                
                print(message[0], end = "")
                main(message[1:])
                
            elif message[0] == "z":
                print(chr(ord(message[0])-25), end = "" )
                main(message[1:])
            else:
                print(chr(ord(message[0]) + 1), end = "")
                main(message[1:])
            
    else:
        print(message)
            
message = input("Enter a message:\n")
print("Encrypted message:")
main(message)