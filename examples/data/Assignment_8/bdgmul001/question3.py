# program that uses a recursive function to encrypt a message by converting all lowercase characters to the next character
# Mulisa Badugela
# BDGMUL001
# 08 MAY 2014

message = input("Enter a message:\n")  # input message to be encrypted

def encrypt(message):
    if message =="": # base case
        return ""
    
    else:
        order = ord(message[0]) +1 # convert a letter to its corresponding order and add 1 to that order value
        character = chr(order)     # conver the new order value above to its corresponding character
        if message[0] == ' ':
            character = chr(order-1) 
        else:
            if message[0] == 'z':    # changing 'z' to 'a' because there ord('z')+1 is not a letter
                character = 'a'
            elif message[0] < chr(97):
                character = message[0]
            else:
                character = chr(order)                
        
        print (character,end="")
        return encrypt(message[1:])
    

print('Encrypted message:')
print(encrypt(message))