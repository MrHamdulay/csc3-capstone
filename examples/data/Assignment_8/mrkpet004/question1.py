"""program with a recursive function to calculate whether or not a string is a palindrome
peter m muriuki
9/5/14"""

def reverse(string):
    # base case - empty string
    if len(string)==0:
        return string
    # recursive step
    else:
        return reverse(string[1:]) + string[0]

string=input("Enter a string:\n")
s_not="Not a palindrome!"
s_is="Palindrome!"
def palstr(string):
    if string=="":
        return s_not
    elif string==reverse(string):
        return s_is
    else:
        return s_not

print (palstr(string))