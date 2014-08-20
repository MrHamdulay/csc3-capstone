"""A8Q1 - Palindrome
5/3/2014
CRNKEE002"""

def main():
    word = input('Enter a string:\n')
    is_palindrome(0, len(word)-1, word)
    
def is_palindrome(start, end, string):
    if string[start] != string[end]:
        print ('Not a palindrome!')
    elif start >= end:
        print ('Palindrome!')
    elif string[start] == string[end]:
        return is_palindrome(start +1, end -1, string)
    
if __name__ == '__main__':
    main()