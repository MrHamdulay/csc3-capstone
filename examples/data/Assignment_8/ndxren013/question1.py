"""reneshan naidoo
ndxren013
7 may 2014"""
def isPalindrome(word):
#test for base case    
    if len(word)== 1 or len(word)==0: #if word only has one letter it is already a palindrome
        return True
    else:
        if word[0]==word[-1]:
            return isPalindrome(word[1:-1])#testing the "second layer" of the string
        else:
            return  False #when word is not palindrome

def main ():

    user = input("Enter a string:\n")

    if (isPalindrome(user) == True):

        print("Palindrome!")

    else:

        print("Not a palindrome!")

main()

