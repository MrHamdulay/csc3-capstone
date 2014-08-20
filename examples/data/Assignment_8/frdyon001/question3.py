"""YONELA FORD
FRDYON001
04 MAY 2014"""
#get an input from the user
message=input("Enter a message:\n")
def encrypt(message):
    #if my message is empty then return an empty string
    if len(message)<1:
        return " "
    #if the character is not a lower case alphabet, then keep it the same and check the rest of the string
    elif message[0].islower()==False:
        return message[0]+ encrypt(message[1:])
    # if the character is a "z" change it to an "a"
    elif message[0]=="z":
        return "a"+ encrypt(message[1:])
    # change the character to the next ASCII value and keep checking the characters afterwards
    else:
        new_chrtr=(ord(message[0])+1)
        return chr(new_chrtr) + encrypt(message[1:])
print("Encrypted message:")    
print(encrypt(message))