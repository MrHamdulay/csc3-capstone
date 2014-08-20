# program to encrypt a message by converting each letter to the letter that comes after it in the alphabet
# khadeejah omar
# 7 may 2014

encrypted_message = ""

def main() :
    message = input("Enter a message: \n")
    print(encrypt(message))

def encrypt(message) :
    
    global encrypted_message
    
    # base case
    if message == "" :
        return ("Encrypted message: \n" + encrypted_message)
    
    # recursive step
    else : 
        
        if 97 <= ord(message[0]) < 122 : # if it is a lowercase letter between "a" inclusive, and "z", perform encryption (ordinal values of "a" and "z" are 97 and 122, respectively)
                encrypted_letter_number = ord(message[0]) + 1 # add 1 to the ordinal code of character to determine the ordinal code of encrypted character
                encrypted_letter = chr(encrypted_letter_number) # convert the ordinal code to its encrypted character
                encrypted_message += encrypted_letter # add the encrypted character to the encrypted message
                return (encrypt(message[1:]))
            
        elif message[0] == "z" : # if the letter is "z", add "a" to the encrypted message
            encrypted_message += "a"
            return (encrypt(message[1:]))
        
        else : # if the character is a punctuation mark, empty space or uppercase letter - add the character unencrypted to the encrypted message
            encrypted_message += message[0]
            return (encrypt(message[1:]))
            
        
main()