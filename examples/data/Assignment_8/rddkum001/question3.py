"""Converting to the next character
Kumaran Reddy
9 May 2014"""

message=input("Enter a message:\n")
def convert(message):
    if len(message) == 0:
            return ''
    else:
        if message[0].isalpha()==False: #To check if first character is an alphabet-base test
            return message[0] + convert(message[1:]) #returns non_alphabet and checks next character
                
        elif message[0].isupper()==True: #To check if character is a capital letter-base test
            return message[0] + convert(message[1:]) #returns capital letter and checks next letter
            
        elif message[0] == 'z': #checks if character is a 'z',then must be changed to 'a'
            return 'a' + convert(message[1:])
            
        elif message[0] == ' ': #Checks if there is a space
            return ' ' + convert(message[1:]) #returns space and then checks next character
            
        else:
            return chr(ord(message[0])+1) + convert(message[1:]) #will change the unicode by moving the value one forward,and then check rest of message   
            
print("Encrypted message:")
print(convert(message))
