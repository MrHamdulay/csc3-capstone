"""program about something strange
mr luci
09 May"""

s=input("Enter a string:\n")
if s == '':
    print("Palindrome")
else:
    if (ord(s[0]) - ord(s[len(s)-1])) == 0:
        # v-- forgot this here
        print("Palindrome!")
    else:
        print("Not a palindrome!")