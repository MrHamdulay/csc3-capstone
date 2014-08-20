

#s for sentence
def reverse(s):
    index=len(s)-1
    if len(s)==1:
        return s
    elif len(s)==0:
        return 0
    else:
        return s[index] + reverse(s[:index])
    
#ckeck if reversed string =original string    
def check(s):
    if s!="":
        if s==reverse(s):
            return "Palindrome!"
        else:
            return "Not a palindrome!"
    elif s=="":
        return ""
    
s=input("Enter a string:\n")
print(check(s))
    