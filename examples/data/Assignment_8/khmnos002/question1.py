"""program to calculate palindromes using recursion
nosipho khumalo
04 May 2014"""



def palindrome(word):
    if len(word) <= 1:
        return "Palindrome!"
    elif (ord(word[0]) - ord(word[len(word)-1])) == 0:
        return palindrome(word[1:len(word)-1])
    else:
        return "Not a palindrome!"

word = input("Enter a string: \n")
print(palindrome(word))
    