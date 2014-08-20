""" Program to determine whether a string is a palindrome or not
Axel du Plessis
09/05/2014"""

def palindrome(message):
    if len(message)==0 or len(message) == 1:
        return True
    if message[0]==message[-1]:
        return palindrome(message[1:-1])
    else:
        return False

message = input("Enter a string:\n")
if palindrome(message):
    print("Palindrome!")
else:
    print("Not a palindrome!")