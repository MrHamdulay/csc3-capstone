# This is a python program that uses a recursive function to encrypt a message 
# by converting all lowercase characters to the next character (with z transformed to a).

# Student Name: Simeon Nandjembo

# Student Number: NNDSIM001

# 05 May 2014

def encrypt(string): 
    """encrypt a message by converting all lowercase characters to the 
    next character (with z transformed to a) by using recursion"""
    
    if string == "":      
        return string # Base case: empty string
    elif not string[0].isalpha() or not ord(string[0]) in range(97,123):
        # Exempt encrypting non alphabetical characters
        # with ordinary values out of the range of lower case alphabetica characters
        return string[0] + encrypt(string[1:])
    elif string[0] != "z": 
        # Encrypt each character to the next in the alphabet sequence
        return chr(ord(string[0]) + 1) + encrypt(string[1:])
    else:
        # If the next charater is "z", encrypt it to "a"
        return "a" + encrypt(string[1:])
        
    
def main():
    
    phrase = input("Enter a message:\n")
    
    # Encrpt the phrase after converting it to lower case
    print("Encrypted message:",encrypt(phrase),sep='\n')


if __name__ == "__main__":
    main()


#Sample I/O:
    
#Enter a message:
#hello world
#Encrypted message:
#ifmmp xpsme