"""Program using recursion to determine if a string is a palindrome.
Kemeshan Naicker
4 May 2014"""

#Prompt user for string. (Outside of function so user is not prompted for an input with every repetition.)

string = input("Enter a string:\n")

def is_pal(string):
    #If the length of the string in question is 3 or less, and if the first and last character are the same,
    #then the string, is a palindrome.
    if string[0] == string[len(string)-1] and len(string) <= 3:
        print("Palindrome!")
    
    #If the first and last characters of a string are the same but the length is more than 3, strip away the
    #first and last character and re-analyse.
    elif string[0] == string[len(string)-1]:
        return is_pal(string[1:len(string)-1])
    
    #If the first and last characters are not the same, the string is not palindromic.
    else:
        print("Not a palindrome!")
        
if __name__=="__main__":
    is_pal(string)
        