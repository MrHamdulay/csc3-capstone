"""Adam Kaliski KLSADA002
CSC1015F Assignment 8 Q1
2014-05-06
Recursive function to test if string is a palindrome"""
def isPalindromic(strng):
    if strng == '':
        print('Palindrome!')
    elif len(strng) == 1:
        print('Palindrome!')
    elif strng[0:1] == strng[len(strng)-1:len(strng)]:
        isPalindromic(strng[1:len(strng)-1])
    else:
        print('Not a palindrome!')

if __name__ == '__main__':   
    wrd = input("Enter a string:\n")
    isPalindromic(wrd)