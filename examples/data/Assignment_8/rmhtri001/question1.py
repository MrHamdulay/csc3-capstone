string = input("Enter a string:\n")

if string == '':
    print(string)
else:
    if (ord(string[0]) - ord(string[len(string)-1])) == 0:
        print("Palindrome!")     
    else:
        print("Not a palindrome!")