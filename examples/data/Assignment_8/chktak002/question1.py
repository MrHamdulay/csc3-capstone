s=input("Enter a string:\n")
def palindrome(s):
    
        if s==" " or s=="": #base case 
                return ""
        else:
                return s[-1] + palindrome(s[0:len(s)-1]) #recurses letter by leter and returns the reverse of the string 
    
rev = palindrome(s)

if rev == s:
        print("Palindrome!")
else:
        print("Not a palindrome!")
    