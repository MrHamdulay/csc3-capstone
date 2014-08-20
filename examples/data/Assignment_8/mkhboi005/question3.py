"""MKHBOI005
5 May 2014
Assignment 8 Question 3"""

message=input("Enter a message:\n")
def encode(message):
#base case return empty string if string is empty
    if len(message)<1:
        return " "
# keep lower case letters the same
    elif message[0].islower()==False:
        return message[0]+ encode(message[1:])
# change 'z' to 'a'
    elif message[0]=="z":
        return "a"+ encode(message[1:])
    else:
        new_chrtr=(ord(message[0])+1)
        return chr(new_chrtr) + encode(message[1:])
print("Encrypted message:")    
print(encode(message))