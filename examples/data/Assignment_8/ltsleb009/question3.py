'''Encrypts a message'''

string = input("Enter a message:\n")

def encrypt(string):
    """converts each lower case to the next letter in the alphabets"""
    
    #checks for if string is blank
    if string:
        if string[0] == 'z':
            #change z to a 
            return('a' + encrypt(string[1:]))
        
        elif  97 <= ord(string[0]) < 122:
            
            new_ordinal = ord(string[0]) + 1 #increment ord of old chr by 1
            return chr(new_ordinal) + encrypt(string[1:]) #recursive step
        else:
            return(string[0] + encrypt(string[1:])) #recursive step
    else: # if string is blank
        return("")  
print("Encrypted message:\n{}".format(encrypt(string)))