"""Program using recursion to determine if a string is a palindrome
thushar hariparsad 
4 May 2014"""

string = input("Enter a string:\n")

def is_palindrome(string):
   #if the string has 3 or less characters then it is a palindrome if the first and last characters are the same
    if string[0] == string[len(string)-1] and len(string) <= 3:
        print("Palindrome!")
    
    #If the first and the last characters are same but length of string is greater than 3, remove the first and last characters and check again
    elif string[0] == string[len(string)-1]:
        return is_palindrome(string[1:len(string)-1])
    
    #If the first and last characters are different then it is not a palindrome
    else:
        print("Not a palindrome!")
        
if __name__=="__main__":
    is_palindrome(string)
        