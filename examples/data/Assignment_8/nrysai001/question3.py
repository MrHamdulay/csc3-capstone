# question3
# saiheal narayan
# 10 may 2014

def messages():#inputs
    
    
    message = input("Enter a message:\n")
    
    return message

def encrypt(message):
    
    
    if len(message) == 0:
        return ''
    else:
        if message[0].isalpha()==False:
            return message[0] + encrypt(message[1:])
            
       
        
        elif message[0].isupper()==True:
            return message[0] + encrypt(message[1:])
        
        
        elif message[0] == 'z':
            return 'a' + encrypt(message[1:])
        
        
        elif message[0] == ' ':
            return ' ' + encrypt(message[1:])
        
        else:
            return chr( ord(message[0])+1 ) + encrypt(message[1:])
       
    
def main():
     
    
    message = messages()
    encrypted = encrypt(message)
    
    print("Encrypted message:")
    print(encrypted)
    
main()
    