''' a Python program with a recursive function to calculate whether or not a string is a palindrome
sankara mallane
5 may 2014
'''

#a function to check if a string is a palindrome
def palindrome(message):
    # check the lengh of message
    if len (message) < 2:
        # if message satisfies the if statement return palindrome
        return "Palindrome!"
    
    # check the length of message
    if len (message) >= 2:
        # run through the message comparing first with last letter
        if message[0] == message[-1]:
            
            return palindrome(message[1:-1])
        
        # message is not a palindrome    
        else:
                return "Not a palindrome!"
# user input        
message = input("Enter a string:\n")

print(palindrome(message))