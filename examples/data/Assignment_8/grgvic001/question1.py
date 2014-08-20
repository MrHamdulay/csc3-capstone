#check palindrome strings using recursion
#victor gueorguiev
#03 May 2014

def reverse_str(x):
    if x == '':
        return ''
    else: return x[-1] + reverse_str(x[:-1])
    
def main():
    sinput = input('Enter a string:\n')
    if sinput == reverse_str(sinput):
        print('Palindrome!')
    else:
        print('Not a palindrome!')
        
main()