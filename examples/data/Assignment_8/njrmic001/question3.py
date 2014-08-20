#A program that encypts a message by converting all lowercase letters to the next letter in the alphabet
#Author: Michelle Njoroge
#Date: 10 April 2014

message=input("Enter a message:\n")
def cryptic(message):
    if len(message)<=1:
        if message.isalpha():
            if message.isupper():
                return message
            else:
                if message=="z":
                    message="a"
                    return message
                else:
                    message=chr(ord(message)+1)
                    return message
        else:
            return message
    else:
        if message==" ":
            return message
    
        letter=message[0]
        if letter==" ":
            return letter+cryptic(message[1:])  
    
        else:
            if letter=="z":
                letter="a"
                return letter+cryptic(message[1:])          
            else:
                if letter.isupper():
                    return letter+cryptic(message[1:])
                else:
                    letter=chr(ord(letter)+1)
                    return letter+cryptic(message[1:])
              
    

print("Encrypted message:")
print(cryptic(message))


        