'''Palindromic words - Assignment 8
Julian Albert
08-05-2014'''

message = input("Enter a string:\n")

def palindrome(message):
    if message == '':
        return ("Palindrome!")
    else:
        if (ord(message[0]) - ord(message[len(message)-1])) == 0:#runs through string checking if first character is equal to the last
            return palindrome(message[1:len(message)-1])
        else:
            return ("Not a palindrome!")#if characters are not the same, then it is not a palindrome
        
print(palindrome(message))

            
            
        
        
    
