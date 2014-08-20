def is_palindrome(inpt):
    if inpt == "":
        return True
    elif inpt[0] == inpt[len(inpt) - 1]:
        return is_palindrome(inpt[1:len(inpt) - 1])
    else:
        return False


str_inpt = input("Enter a string:\n")
if is_palindrome(str_inpt):
    print("Palindrome!")
else:
    print("Not a palindrome!")