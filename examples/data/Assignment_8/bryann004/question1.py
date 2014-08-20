# anna borysova
# q1, ass8
# 2014 - 05 - 06

string = input("Enter a string:\n")

i = 0
def reverse(string, i):
    if i == len(string)-1:
        return string[i]
    return reverse(string, i+1) + string[i]

if reverse(string, i) == string:
    print("Palindrome!")
else:
    print("Not a palindrome!")