"""Palindrome
Michelle Lu
4 May 2014"""



words=input("Enter a string:\n")

def palindrome(words):
        
        if len(words)<=1:
                print("Palindrome!")
        elif words[0]==words[-1]: #if first letter == last letter
                return palindrome(words[1:-1]) 
        else:
                print("Not a palindrome!")
                

palindrome(words)
        
    