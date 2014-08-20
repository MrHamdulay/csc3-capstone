"""Assignment 8 Question 3
James Lloyd
4 May 2014"""

#Retrieving message
message = input ("Enter a message:\n")

def encrypt (message):
    """Function to shift letters by plus one"""
    #Setting the base case
    if message == '':
        return ''
    #Changing the first character to code the adding to the code of the rest of the string. 
    else:
        #Setting to keep spaces
        if message [0] == ' ':
            return ' ' + encrypt (message [1:])
        #setting z to a
        elif message [0] == "z":
            return "a" + encrypt (message [1:])
        else:
            if 97 <= ord (message [0]) <= 121:
                ASCII = (ord (message [0])) + 1
                code = chr (ASCII)
                return code + encrypt (message [1:])    
            else:
                return message [0] + encrypt (message [1:])

#Printing encrypted message  
print ("Encrypted message:")
print (encrypt (message))