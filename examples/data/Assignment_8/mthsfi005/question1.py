def backward(s):
    if s=='':
        return ''
    
    else:
        return backward(s[1:]) + s[0]
    
def main():
    c = input('Enter a string:\n')
    if c == backward(c):
        print('Palindrome!')
        
    else:
        print('Not a palindrome!')
        
main()