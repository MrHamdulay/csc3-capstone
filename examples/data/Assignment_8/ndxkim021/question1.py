#Kimberley Naidoo
#6 May 2014
#Recursion Testing_ Palindrome strings

def lower(a):   #Convert entered string to lowercase
    a = a.lower()
    return a

def isPal(a): #Method to test if palindrome
    if len(a) <= 1:
        return True
    if a[0] == a[-1]: #test if first and last letter are the same
        return isPal(a[1:-1])  

def isPalindrome(a): #Return result to be printed
    if isPal(lower(a)) == True: 
        print("Palindrome!")
    else:
        print("Not a palindrome!")
        
a = input("Enter a string: \n")
x = lower(a)
y = isPal(a)
z = isPalindrome(a)


