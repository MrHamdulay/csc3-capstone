#Jono Field
#May 10 
#Question 3


def encrypted_message(y):
    if len(y) == 1:
        if y.islower():  #checking that the string is lowercase
            
            
            if y == 'z': 
                return 'a' #returning a value for 'z' to 'a'
            else:
                return chr(ord(y) + 1)   #assigning the ord value of one character, to the next ord of the next character
        else:
            return y
    else:
        return encrypted_message(y[0]) + encrypted_message(y[1:])


Str = input("Enter a message:\n")
print("Encrypted message:")
print(encrypted_message(Str))