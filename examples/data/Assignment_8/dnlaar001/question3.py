'''Question3 
5 may 2014
aaron daniels'''
def main():
    y=input('Enter a message:\n')
    print('Encrypted message:\n')
    lala(y)
    
def lala(x):
    if len(x)>0:
        r=chr(ord(x[0])+1)
    else:
        ()
    return r + lala(x[1:])

main()