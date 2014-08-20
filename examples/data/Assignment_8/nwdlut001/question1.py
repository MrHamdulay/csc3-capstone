s=input("Enter a string:\n")
if s=="":
    print("")
elif s[0]==s[-1] and s[1]==s[-2] and s[2]==s[-3]:
    print("Palindrome!")
elif s[0]!=s[-1] or s[1]!=s[-2] or s[2]!=s[-3]:
    print("Not a palindrome!")