#Program that uses a recursive function to encrypt a message by converting all lowercase characters to the next character 
#Kiran Desraj - DSRKIR001
#5 May 2014

#User is prompted to enter a message

original_message = input('Enter a message:\n')

string = ''

def secret(message):
    
    global string
    if message == '':
        return string
 
 #moves letters one letter forward   
    
    elif  96 < ord(message[0])  and  122 > ord(message[0]):
        
        string = string + chr(ord(message[0])+1)
        
        return secret(message[1:len(message)])
        
#moves z to a    

    elif (ord(message[0]) == 122):
        
        string = string+'a'
        
        return secret(message[1:len(message)])
    
    else:
        
        string = string + message[0]
        
        return secret(message[1:len(message)])

# Prints encrypted message

print('Encrypted message:')
print(secret(original_message))
        












