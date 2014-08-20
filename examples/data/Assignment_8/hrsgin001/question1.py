#Gina Horscroft
#Question 1
#check string is a palindrome

def pal(s):
    if s == "":
        return True
    else:
        if s[0] == s[len(s)-1]:
            return pal(s[1:(len(s)-1)])
        else:
            return False
        
s = input("Enter a string:\n")
if pal(s):
    print("Palindrome!")
else:
    print("Not a palindrome!")