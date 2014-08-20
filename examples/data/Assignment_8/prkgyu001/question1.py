
def reversed_string(s):
    if len(s) == 1:
        return s
    else:
        return s[-1] + reversed_string(s[:-1])


string = input("Enter a string:\n")
if reversed_string(string) == string:
    print("Palindrome!")
else:
    print("Not a palindrome!")
