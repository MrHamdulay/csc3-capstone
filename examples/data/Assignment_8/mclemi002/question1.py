"""emile mclennan
6/5/14
A8 Q1"""

def palindrome(s):
    if s == '':
        print("Palindrome!")
    else:
        if (ord(s[0]) - ord(s[len(s)-1])) == 0:
            return palindrome(s[1:len(s)-1])
        else:
            print("Not a palindrome!")
            
word = input("Enter a string:\n")
palindrome(word)