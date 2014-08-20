''' Program to identify a palidrome
Yongama Giwu
05/08/2014 '''
def palidrome(s):
    if s=="":
        return ""
    else:
        return s[-1] + palidrome(s[:-1])
string= input("Enter a string:\n")
pal=palidrome(string)
if string == pal:
    print("Palindrome!")
else:
    print("Not a palindrome!")
