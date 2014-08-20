__author__ = "JNSJOH014"
"""Using recursion to determine if a string is palindromic"""
def pal(s):
    if len(s)<2:
        return True
    elif s[0]==s[-1]:
        return pal(s[1:-1])
    else:
        return False
if __name__=="__main__":
    s = input("Enter a string:\n")
    if pal(s):
        print("Palindrome!")
    else:
        print("Not a palindrome!")