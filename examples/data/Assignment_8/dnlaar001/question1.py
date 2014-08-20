'''Question1 
5 may 2014
aaron daniels'''
def main():
    y=input('Enter a string:\n')
    if y==lala(y):
        print('Palindrome!')
    else:
        print('Not a palindrome!')
        
def lala(x):
    if x=='':
        return x
    else:
        return lala(x[1:])+x[0]
    
main()