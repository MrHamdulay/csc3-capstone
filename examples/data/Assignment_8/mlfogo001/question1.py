''' a Python program with a recursive function to calculate whether or not a string is a palindrome
OhGee
5 may 2014
'''

#define function message
def palindrome(message):
    if len (message) < 2:
        return "Palindrome!"
    
    if len (message) >= 2:
        if message[0] == message[-1]:
            
            return palindrome(message[1:-1])
            
        else:
                return "Not a palindrome!"
        
message = input("Enter a string:\n")

print(palindrome(message))