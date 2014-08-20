#dean makambwa
#6/05/14
#prog for checking if a string is a palindrome

x=input('Enter a string:\n')

def palindrome(x):
    #if input is empty or a space return a nothing or an empty string
    if x=='':
        return'' 
    elif x==' ':
        return ' '
    
    #if input is a string check the string the go through the string and reverse 
    else:
        return x[-1]+ palindrome(x[0:len(x)-1])
#set a variable as the function and use it to check whether what is returned is a palindrome or not     
m = palindrome(x)
if m==x:
    print('Palindrome!')
else:
    print('Not a palindrome!')
    
