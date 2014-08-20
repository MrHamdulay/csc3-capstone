# program to encrypt a message
# mllgad001
# 8 April 2014

def encrypt(s):    # define function for encrypted message
        
        if s =='':                 # base case- if input is an empty string, return an empty string
                return ''
        
        elif 97 <= ord(s[0]) < 122:        # if the letters is between a and z (not including z) and lower case
                new_message = ''
                new_letter = chr(1+ ord(s[0]))   # converts the letter to the next one 
                new_message += new_letter            # adds new letter to empty string
                print(new_message, end ='')          # prints the new letters
                return (encrypt(s[1:]))           # recurse over the rest of the string
        
        elif s[0] == 'z':                     # if the letter is z, replace it with an a
                new_message = ''
                new_letter = "a"
                new_message += new_letter            # adds new letter to empty string       
                print(new_message, end = '')       
                return (encrypt(s[1:]))            # recurse over rest of string
        else:                          
                new_message = ''                   # if the character is anything besides a lower case letter
                new_letter = s[0]
                new_message += new_letter       # leaves the character as it is
                print(new_message, end = '')
                return encrypt(s[1:])
        
def message():
        s = input("Enter a message:\n")
        print("Encrypted message:")
        print(encrypt(s))
    
message()

