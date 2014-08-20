"""recursive palindrome checker program
casey o'donnell
5 may 2014"""

def pal_check(s):
    if not s:
        return True    
    elif s[0]==s[-1]:
        return pal_check(s[1:-1])
    else:
        return False
    

s=input("Enter a string:\n")
if pal_check(s):
    print("Palindrome!")
else:
    print("Not a palindrome!")