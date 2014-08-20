"""Palindrome detectooooooorrr (recursion)
Charlie Shang
8 May 2014"""

#input the string to be tested
string = input("Enter a string:\n")

def is_palindrome(string):
    #exception handling (if length < 3, then only test if first letter = last letter)
    if string[0] == string[-1] and len(string) <= 3:
        print("Palindrome!")    
    
    #If length > 3 and first and last letter is the same, strip away the first and last letter and re-evaluate
    elif string[0] == string[-1]:    
        return is_palindrome(string[1:-1])
    
    #If the first letter != last letter, then its not a palindrome.
    else:
        print("Not a palindrome!")
        
if __name__=="__main__":
    is_palindrome(string)
        