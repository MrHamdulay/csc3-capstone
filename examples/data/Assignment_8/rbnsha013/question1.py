"""To see whether a string is a palindrome
Shane Robinson
3 May 2014"""

print("Enter a string:")
string = input()

def palindrome(string):
    if len(string)<2:
        return True
    elif string[0]!=string[-1]:
        return False
    else:
        return palindrome(string[1:-1])

check = palindrome(string)
if check:
    print("Palindrome!")
else:
    print("Not a palindrome!")