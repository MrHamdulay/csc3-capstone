"""encrypt a message by converting all lowercases letters to the next character using recursion
joshua wort
5 May 2014"""

def encrypted(message):
    #base case
    if message=="":
        return message
    #checks if character is uppercase
    elif message[0]==message[0].upper():
        return message[0]+ encrypted(message[1:])
    #checks if character is not part of the alphabet
    elif not message[0].isalpha():
        return message[0] + encrypyted(message[1:])
    #checks if character is "z" and if so converts it to "a"
    elif message[0]=="z":
        return "a" + encrypted(message[1:])
    else:
        return chr(ord(message[0])+1) + encrypted(message[1:])
    
message = input("Enter a message:\n")
print("Encrypted message:\n", encrypted(message), sep="")
    
