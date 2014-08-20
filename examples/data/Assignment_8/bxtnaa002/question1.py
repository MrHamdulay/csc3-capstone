# question1.py
# author: bxtnaa002
# May 2014

s = input("Enter a string:\n")
def reverse(s): 
        if s == "":
                return s
        else:
                return reverse(s[1:]) + s[0] #reverses the string after the current letter position
        
def palin(s):
        y = reverse(s) #y is the reversed string, if it the same as the original the string is a palindrom
        if y == s:
                return "Palindrome!"
        else:
                return "Not a palindrome!"
print(palin(s))