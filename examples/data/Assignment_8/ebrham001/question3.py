'''Recursive function that encrypts a message
HAMZA EBRAHIM
05/05/2014'''

# Assignment 8 - Question 3

# recursive function which encrypts a message. It converts all letters to the next letter in the alphabet with z becoming a 

def encryp(unencrypted, encrypted, count, number):
    if count < number:
        
        old = unencrypted[count]
        if old == 'z':
            encrypted += 'a'
        elif (old == ' '):
            encrypted += ' '
        elif (old.isalpha() == False):    
            encrypted += old
        elif old.isupper():
            return unencrypted

        else:
            code = ord(old) + 1
            encrypted += chr(code)
            
        count += 1
        return encryp(unencrypted, encrypted, count, number)
    
    
    else:
        return encrypted

# main function which prompts user for the message to encrypt, invokes the encryp function above    
    
def main():
    unencrypted = input("Enter a message:\n")
    encrypted = ''
    number = len(unencrypted)
    print("Encrypted message:\n",encryp (unencrypted, encrypted, 0, number), sep='')
    
    
main()    

# program ends