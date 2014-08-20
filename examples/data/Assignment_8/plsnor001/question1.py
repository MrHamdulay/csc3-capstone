'''Calculate whether or not a string is a palindrome
Noko Pilusa
04 May 2014'''

def palin(string):
    #check for number of characters in string
    if len(string)<2:
        return print('Palindrome!')
    
    #compare last word or character to the first
    if string[0] != string[-1]:
        return print('Not a palindrome!')
    
    return palin(string[1:-1])#recurse


palin(input('Enter a string:\n'))