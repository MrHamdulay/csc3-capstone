"""reverse string programme
Annie Ho
9 May 2014"""

def rvrs(p):
    if len(p) == 1:
        return p
    else:
        return p[-1] + rvrs(p[:-1])


string = input("Enter a string:\n")
if rvrs(string) == string:
    print("Palindrome!")
else:
    print("Not a palindrome!")