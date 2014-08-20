def palindrome(x, s):
    if x >= len(s):
        return True
    if (s[x] != s[-x-1]):
        return False
    return palindrome(x+1, s)

a = input("Enter a string:\n")
if palindrome(0, a):
    print("Palindrome!")
else:
    print("Not a palindrome!")
