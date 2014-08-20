"""PRIYANKA GOBERDHAN
8 MAY 2014
Palindrome"""


string=input("Enter a string:\n")

def check(string):
    if string == '':
        return True

    else:
        if (ord(string[0]) == ord(string[len(string)-1])):
            return check(string[1:len(string)-1])

        else:
            return False

if(check(string)==True):

    print("Palindrome!")

else:

    print("Not a palindrome!")