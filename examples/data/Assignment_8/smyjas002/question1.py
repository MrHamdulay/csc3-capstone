#Jason Smythe
#assignment 8
#question 1

def isPalindrome( testStr ):
	# base case, used if gone through whole string withought issue. 
    if len (testStr) < 1:
        return "Palindrome!"
    # first recursive step, checks if the first and last letter is the same.
    elif testStr[0] == testStr[-1]:
        return isPalindrome(testStr[1:len(testStr) - 1])
    # second recursive step, if it does not match it is not a palindrome.
    else:
        return "Not a palindrome!"
            
def main():
	a = input("Enter a string:\n")
	print(isPalindrome(a))

main()

'''
Sample I/O:

Enter a string:
able was I ere I saw elba
Palindrome!

Sample I/O:

Enter a string:
elba is a noob
Not a palindrome!
'''
