#KNNSAD001
#Assignment 8
#Program that uses a recursive function to encrypt a message by converting all lowercase characters to the next character(with z transformed to a) 


#TEXT INPUT IS INSERTED

message_1 = input('Enter a message:\n')
text = ''

def secret(message_2):
    
    global text
    if message_2 == '':
        return text
 
#CHANGES THE ORDER OF LETTERS- LETTERS ARE MOVED ONE FORWARD   
    
    elif  96 < ord(message_2[0])  and  122 > ord(message_2[0]):
        text = text + chr(ord(message_2[0])+1)
        return secret(message_2[1:len(message_2)])
        
#TRANSFORMS Z TO A    

    elif (ord(message_2[0]) == 122):
        text = text+'a'
        
        return secret(message_2[1:len(message_2)])
    
    else:
        text = text + message_2[0]
        return secret(message_2[1:len(message_2)])

#PRINT STATEMENTS--ENCRYPTED STATEMENT IS DISPLAYED
print('Encrypted message:')
print(secret(message_1))
        












