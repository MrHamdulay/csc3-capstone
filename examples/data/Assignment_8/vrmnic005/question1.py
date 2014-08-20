#VRMNIC005
#Assignment 7, question 1

def palindrome(string):
    if len(string) <= 1:
        return True
    elif string[0] == string[-1]:
        return palindrome(string[1:-1])
    else:
        return False

string = input("Enter a string: \n")

if palindrome(string):
    print("Palindrome!")
else:
    print("Not a palindrome!")

