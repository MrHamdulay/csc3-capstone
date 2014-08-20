#check if string is palindrome
#julia breakey
#6 may 2014

#check if palindrome general function
def palindrome(word):
    if len(word)==1 or len(word)==0:
        return True
    elif word[0]==word[-1]:
        palindrome(word[1:-1])
        return palindrome(word[1:-1])
    else: 
        return False
    
#ask for string    
string=input("Enter a string:\n")

#check if palindrome specific string
if palindrome(string)==True:
    print("Palindrome!")
else: print("Not a palindrome!")    