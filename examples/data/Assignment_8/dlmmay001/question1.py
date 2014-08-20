def pali(x):
    
    if len(x) < 2: #or len(x) == 0:
        return 'Palindrome!'
   
    elif x[0] == x[-1]:
        #x=x[1:-1]
        return pali(x[1:-1])
    
    else:
        return 'Not a palindrome!'
    
x = input('Enter a string:\n')  

def main():
    
    print(pali(x))
    
main()