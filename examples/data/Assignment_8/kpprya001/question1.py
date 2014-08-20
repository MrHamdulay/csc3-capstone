word = input("Enter a string:\n")
#create two strings to compare
string1 = word
string2 = string1
#find length of both strings for working out later on
lenString1 = len(string1)
lenString2 = len(string2)
isPalindrome = True
def find_palindrome(string1,string2):
    #if the string is not blank, then carry on
    if (string1!=""):
        if(string1[0:1]==string2[-1:]):
            isPalindrome = True
            return(find_palindrome(string1[1:],string2[:len(string2)-1]))
        else:
            isPalindrome = False
            return isPalindrome
    else:
        isPalindrome = True
        return isPalindrome
     
    
    
#print a statement dependent on the boolean (isPalindrome ) that is returned   
if(find_palindrome(string1,string2)):
    print("Palindrome!")
else:
    print("Not a palindrome!")
    
 #and string1[0:1]==(" ") and string1[:lenString2-1]
    
    