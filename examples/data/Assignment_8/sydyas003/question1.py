#Yaseen Sayed Ismail
#SYDYAS003
#09/05/2014
#Checks palindrome

def palindrome(a):
    if(a==""):
        return True
    else:
        if(a[0]==a[len(a)-1]):
            return palindrome(a[1:len(a)-1])
        else:
            return False

a=input("Enter a string:\n")
if(palindrome(a)):
    print("Palindrome!")
else:
    print("Not a palindrome!")