# a program that uses a recursive function to encrypt a message by converting all lowercase characters to the next character 
#Jenny Luo
# 9 May 2014


message=input("Enter a message:\n")


def convert(message):
    new=""
    if message.isupper():#check to see if the message is in upper or lower case
        return message
    if message!="":
        if message[0]!=" ":
            if message[0].isalpha():#check to see if the character is a letter
                if message[0]=="z":
                    string="a"
                else:
                    string=chr((ord(message[0])+1))# adding the character that corresponds to the unicode value 
            else:
                string=message[0]
            new+=string
            new+=convert(message[1:])   # recursive statement
        else:
            new+=" "
            new+=convert(message[1:])#recursive statement
    else:
        new+=""
    return new  #return the final output message

print("Encrypted message:")
print(convert(message))

