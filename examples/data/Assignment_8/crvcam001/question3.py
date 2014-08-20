# question3.py
# program to convert all lower case letters to the next letter in the alphabet using recursion
# camilla craven
# 9 may 2014

string = input("Enter a message:\n")

def encrypt(string):
    
    # if only one letter in string
    if len(string) == 1:
        
        # if string is lower case (capitals remain the same)
        if string.islower(): 
            
            # and if string is the letter z
            if string == 'z': 
                #  z is replaced with a (because no letter after z)
                return 'a' 
            # or if the letter is not z, but is still small letter
            else:
                # use unicode functions to get the next letter in the alphabet
                return chr(ord(string) + 1) 
      
        # if capital letter or punctuation mark
        else:
            # return the same value
            return string
  
    # if string has more than one letter
    else:
        # use recursion to loop through word and change each character
        return encrypt(string[0]) + encrypt(string[1:])

print("Encrypted message:")
print(encrypt(string))