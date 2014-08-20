userInput = input("Enter a string:\n")
f= userInput
s=f
counts = 0
countf = len(f)
pal = True
def palindrome(f,s,pal):
    if(f!="" ):
        if(f[len(f)-1:] == s[:1]):
            return palindrome(f[:len(f)-1],s[1:len(s)],pal)
        else:
            return False
    return True
    
if(palindrome(f,s,pal)):
    print("Palindrome!")
else:
    print("Not a palindrome!")


    #if(f[len(f)-1:] == " "):
                #palindrome(f[:len(f)-1],s,pal)
            #elif(s[:1] == " "):
                #palindrome(f,s[1:],pal)