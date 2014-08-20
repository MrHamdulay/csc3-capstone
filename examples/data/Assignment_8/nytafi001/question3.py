""" A program that uses a recursive function to encrypt a message by converting all lowercase characters to the next character (with z transformed to a).
Author: Afika Nyati
Date: 5th May 2014"""

def encrypt(message):   # A recursive function that encrypts a message by converting all lowercase characters to the next character
    
    
    if message == "" or message == " ":   # The stopping condition occurs when the recursive function reaches the end of the string or if the message is a blank space only.
        
        return ""   # It returns nothing
    
    else:
    
        x = ord(message[:1])    # The first character of the message is converted to its Unicode number.     
    
        if 97 <= x <= 122:   # If the character is between lowercase a (Unicode 97) and lowercase z (Unicode 122), the main part of the recursive function starts.
            
            
            x+=1    # The Unicode of the first character gets incremented with one, to give the Unicode of the character above it.
            
            if x > ord("z"):    # If the new character has a higher Unicode than the last letter of the alphabet (z):
                x -= 26 # The character has 26 minused from it, which is equivalent to looping around the alphabet.
            
            return chr(x) + str(encrypt(message[1:]))   # This part of the recursive function returns back a string of the new converted letter plus the resulting string of the rest of the message (minus the current character), replaced in the same function.
        
        else:   # If the character is not between lowercase a and lowercase z, the recursive funciton is recalled to encrypt the rest of the function.
            return message[:1] + str(encrypt(message[1:]))  # Notice that I add the original character to the string. If the character was a fullstop or a blank space, it will feature in the encrypted message as such.

def main():
    
    message = input("Enter a message:\n")   # Asks user for a message.
    
    print("Encrypted message:\n", encrypt(message), sep = "")   # Prints out the encrypted message.
    

main()