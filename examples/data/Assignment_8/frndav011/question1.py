def palindrome(string):
    if string == "":#Checks if theres no letters left
        return "Palindrome!"
    elif string[0] != string[-1]:#Checks first and last letter
        return "Not a palindrome!"
    elif string[0] == string[-1]:
        return palindrome(string[1:-1])#'Slices' off first and last letter so inner letters can be checked
    

print(palindrome(string = input("Enter a string:\n")))#print statement

