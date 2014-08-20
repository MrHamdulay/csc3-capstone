# A8Q1
def isPalindrome(s, index):
    
    if len(s) == 1:
        return True
    if (index >(len(s)//2)-1):
        return True
    else:
        if s[index] == s[len(s) - 1 - index]:
            return isPalindrome(s, index+1)
        else: 
            return False
           
   
text = input("Enter a string:\n")
if isPalindrome(text, 0) == True:
    print("Palindrome!")
else:
    print("Not a palindrome!")
    
    
    
    
    
    
    
   
