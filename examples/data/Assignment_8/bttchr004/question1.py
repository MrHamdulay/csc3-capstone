"""recursion to find palindrome
chris betteridge
04 may 2014"""

def reverse (n_string):
    #reverse string
    if n_string == "":
        return n_string
    else:
        return reverse(n_string[1:]) + n_string[0]


string = input("Enter a string:\n")
n_string = string.lower()
#test to see if string = reversed string
if reverse(n_string) == n_string:
    print("Palindrome!")

else:
    print("Not a palindrome!")