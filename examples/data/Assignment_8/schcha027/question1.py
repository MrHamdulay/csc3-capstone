# 09/05/2014 
# SCHCH027
# Question1
string=input("Enter a string:\n")
counter=0

#  recursive function to reverse a string
def reverse(string):
    if string=="":
        return string
    else:
        return reverse(string[1:])+string[0]
    
rev=reverse(string)
#checks if original string is the same as reversed string Therefore palindrome
if rev== string:
    print("Palindrome!")
else:
    print("Not a palindrome!")
