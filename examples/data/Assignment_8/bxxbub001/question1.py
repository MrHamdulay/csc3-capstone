def reverse(s):
    if s == "":
        return s
    else:
        return reverse(s[1:])+s[0]


string1 = input("Enter a string:\n")
string2 =reverse(string1)
if string1 == string2:
    print("Palindrome!")
else:
    print("Not a palindrome!")