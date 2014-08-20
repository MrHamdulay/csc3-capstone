"""Program using recursion to determine if a string is a palindrome.
Akhil Singh
4 May 2014"""

#Prompt user for string. (Outside of function so user is not prompted for an input with every repetition.)

str1ng = input("Enter a string:\n")

def is_palindrome(str1ng):
    #If the length of the string in question is 3 or less, and if the first and last character are the same,
    #then the string, is a palindrome.
    if str1ng[0] == str1ng[len(str1ng)-1] and len(str1ng) <= 3:
        print("Palindrome!")
    
    #If the first and last characters of a string are the same but the length is more than 3, strip away the
    #first and last character and re-analyse.
    elif str1ng[0] == str1ng[len(str1ng)-1]:
        return is_palindrome(str1ng[1:len(str1ng)-1])
    
    #If the first and last characters are not the same, the string is not palindromic.
    else:
        print("Not a palindrome!")
        
if __name__=="__main__":
    is_palindrome(str1ng)
        