'''assignment 8, WLSROR002, 7/5/2014'''

#function to reverse the string
def reverse(x):
    if x=='':
        return x
    else:
        return reverse(x[1:])+x[0]
#function to check if the entered string is the same as the reversed string
def main():
    x=input('Enter a string:\n')
    rev=reverse(x)
    if x==rev:
        print('Palindrome!')
    else:
        print('Not a palindrome!')
        
main()
    