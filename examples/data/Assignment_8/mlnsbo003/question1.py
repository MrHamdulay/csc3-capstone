'''palidrome in recursion
Sbongakonke Mlangeni
06 May 2014'''

#taking strings
x = input('Enter a string:\n')
def pal(x):
    #stopping condition
    if x == '':
        return x
    #recursive step 
    else:
        return pal(x[1:]) + x[0]

#printing out the output    
def main():
    if pal(x) == x:
        print('Palindrome!')
        
    else:
        print('Not a palindrome!')
        
main()
    