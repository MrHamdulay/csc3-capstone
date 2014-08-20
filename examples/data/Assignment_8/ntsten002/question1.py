string = input("Enter a string:\n")

def reverse(string):
    if string == "":
        return string
    else:
        new_string = reverse(string[1:])+ string[0]
        return new_string

if reverse(string) == string:
    print("Palindrome!")
else:
    print("Not a palindrome!")