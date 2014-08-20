#Program to check for palindrom*+es
#Kayla Hendricks
#07 May 2014

string=input("Enter a string:\n")

def palindrome(string):
    if string =="":     #if string has no value
        return True
    elif string[0]==string[-1]:     #if first letter equals last letter of string, repeat until string has no value
        return palindrome(string[1:-1])
    else:
        return False

if palindrome(string):          #if palindrome(string) returns true, print
    print("Palindrome!")
else:
    print("Not a palindrome!")
        
    