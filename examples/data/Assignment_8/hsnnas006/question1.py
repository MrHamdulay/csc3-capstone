'''program to determine if a string is a palindrome
nasreen hoosain
06/05/14'''

#recursive function to reverse string
def reverse (string):
    if len(string) == 0:
        return string
    else:
        return string[-1] + reverse(string[0:-1])# reverse string, cut off end character

if __name__=='__main__':
    string = input('Enter a string:\n')
    if string == reverse(string):
        print('Palindrome!')
    else:
        print('Not a palindrome!')