"""
Serayen Govender 
find palindromes
"""

stri=input("Enter a string:\n")
#Enter String

def palindromic(stri):

    if stri == '':
        #all letters reversed

        return True
    #String is a plaindrome

    else:

        if (ord(stri[len(stri)-1])) == ord(stri[0]):
                     #If last and first string are same

            return palindromic(stri[1:len(stri)-1])

        else:

            return False
        #String is not a plaindrome

if(palindromic(stri)==True):

    print("Palindrome!")

else:

    print("Not a palindrome!")