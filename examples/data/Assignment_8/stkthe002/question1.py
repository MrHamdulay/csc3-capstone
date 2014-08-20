#Thea Sitek, STK002
#09.05.2014

def palindrome(check):
    
    length = len(check)
    if length <= 1:
        print('Palindrome!')
        #Will happend in the final round. First:
    else:
        if check[0] == check[-1]:
            check = check[1:-1]
            return palindrome(check)
            #Recursion
        else:
            print('Not a palindrome!')


#Ask for input
sentence = input('Enter a string: \n')
#Call function for that input
palindrome(sentence)

