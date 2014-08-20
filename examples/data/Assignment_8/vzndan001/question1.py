"""recursion: checking palindrmes
danica van der zandt
9 may 2014"""

def palindrome(s):

    if s=="":
        print("Palindrome!")
    elif s[0]==s[-1]:
        return palindrome(s[1:-1])
    
    else:
        print("Not a palindrome!")
    
    
s=input("Enter a string:\n")
palindrome(s)
    

        

        
