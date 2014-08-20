# Cameron Collum
# tests for palindrome
# 05/08/2014

def reverse(p):
    if len(p) == 1:
        return p
    else:
        return p[-1] + reverse(p[:-1])


string = input("Enter a string:\n")
if reverse(string) == string:
    print("Palindrome!")
else:
    print("Not a palindrome!")