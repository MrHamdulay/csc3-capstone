def pal_check(string):
    if string=="":
        return string
    else:
        return pal_check(string[1:])+string[0]
    
words=input("Enter a string:\n")
if words==pal_check(words):
    print("Palindrome!")
else:
    print("Not a palindrome!")