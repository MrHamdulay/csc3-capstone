"""program to calculate if a string is a palindrome
Muhammad Nabeel Dulymamode
08/05/2014"""

def reverse(string):
    #returns the reverse of string
    if len(string) > 0:
        return reverse(string[1:]) + string[0]
    else:
        return ""

string = input("Enter a string:\n")
rev_str = reverse(string)
if rev_str == string:
    print("Palindrome!")
else:
    print("Not a palindrome!")