'''This program uses a recursion function to shows whether or not a string
is palindromique
By Hermann KOUASSI: KSSKOU001
On 3 May 2014'''

def pal(the_str):
    '''check if a given string is palindromic'''
    #in case empty string is the input
    if len(the_str)==0:
        print('Palindrome!')
    #stop condition
    elif len(the_str) == 2 or len(the_str)==3:
        #when first character == last character
        if the_str[0]==the_str[-1]:
            print('Palindrome!')
        #stop checking 
        else:  print('Not a palindrome!')
    #when more than 3 characters in string
    else:
        # call function to carry on checking if same first and last character
        if the_str[0]==the_str[-1]:
            #new string leaves out the first and last characters
            pal(the_str[1:len(the_str)-1])
        else:
            #otherwise stop checking
            print('Not a palindrome!')
        

def main():
    '''main function'''
    #get the string
    the_str = input('Enter a string:\n')
    #call palindromic function 
    pal(the_str)

if __name__=="__main__":
    main()    