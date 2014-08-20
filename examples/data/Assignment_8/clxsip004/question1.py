#Siphesihle Cele
#10 May 2014
#Assignmewnt 8

#3 things needed.
#insert a statement
#loop to check if that statement a palindrom, reads the same from the back.
#print whether it is a palindrom or not.
#the  is_palindrom function does string checking of the word so it can check whether the palindrom argument holds
# main function requests the users input and prints the results.

def is_palindrome(stat):
    if stat == '':
        return 'Palindrome!'
    else:
        if stat[0] == stat[-1]:       # check if first element is the same as last
            return is_palindrome(stat[1:-1])              
        else:
            return 'Not a palindrome!'
        
        
def main():
    user_input = input("Enter a string:\n")
    
    print(is_palindrome(user_input))

main()