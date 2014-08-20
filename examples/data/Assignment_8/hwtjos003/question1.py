"""palindrome checker
Joshua Hewitson
2/5/2014"""

def check_palindrome(input1):
    # input1 is shortened each time so if it is empty then the whole palindrome has been checked and it is a palindrome
    if input1 == "":
        return True
    
    # each end is checked to be the same, if they are, it passes to the next recursion
    if input1[0] == input1[-1]:
        # input is shortened by removing the end characters
        input1 = input1[1:len(input1)-1]
        # check_palindrome is now run again with a shortened input
        if check_palindrome(input1):
            return True
    
    return False

string1 = input("Enter a string:\n")
if check_palindrome(string1):
    print ("Palindrome!")
else:
    print('Not a palindrome!')