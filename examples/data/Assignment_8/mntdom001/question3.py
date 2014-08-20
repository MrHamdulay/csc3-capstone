"""a program that uses a recursive function to encrypt a message by converting
all lowercase characters to the next character (with z transformed to a).
Dominic Manthoko
05 May 2014"""

def move(s):
    """ function that converts each character in a string to the next character """
    
    if s == '':
        return ''
    else:
        l = s[0]           # create a variable l to store the first character of the string
    
        if l.islower() and l.isalpha():       # checks that the letter is in lowercase character
            if l == 'z':
                l = 'a'                # the letter z must become an a
            else:
                l = chr(ord(l)+1)                      # all other must be converted to the next character
        
        return l + move(s[1:])
    
if __name__ == '__main__':
    # prompt the user for imput
    s  = input("Enter a message: \n")    
    
    print("Encrypted message: ")
    print(move(s))