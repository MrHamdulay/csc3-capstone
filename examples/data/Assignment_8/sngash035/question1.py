
def lower(a):   
    a = a.lower()
    return a



def isPal(a): 
    if len(a) <= 1:
        return True
    if a[0] == a[-1]: 
        return isPal(a[1:-1])  



def isPalindrome(a): 
    if isPal(lower(a)) == True: 
        print("Palindrome!")
    else:
        print("Not a palindrome!")
        
        
        
        
        
a = input("Enter a string: \n")
x = lower(a)
y = isPal(a)
z = isPalindrome(a)


