#vhrjoc001

#assignment 8 question 1

#finding a palindrome 

def isPalindrome(s):

    # base case: the empty string and the string with # only one character are both palindromes

            if (len(s) <= 1):

                        return True

    # recursive case: a string whose middle section (everything but # its first and last characher) is a palindrome, and whose first # and last characters are equal, is a palindrome

            elif (isPalindrome(s[1:-1]) and s[0] == s[-1]):

                        return True 

            else:

                        return False

            

string=input("Enter a string:\n")




if isPalindrome(string):

            print("Palindrome!")

else:

            print("Not a palindrome!")


