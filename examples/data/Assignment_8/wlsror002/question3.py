#changes each lowercase letter of the alphabet into the next along (eg a->b) and adds it to a list
def encrypt(x,y):
    if x=='':
        return y
    elif x[0]==' ':
        y.append(x[0])
        return encrypt(x[1:],y)
    elif ord(x[0])<96:
        letter=x[0]
        y.append(letter)
        return encrypt(x[1:],y)
    elif ord(x[0])>122:
        letter=x[0]
        y.append(letter)
        return encrypt(x[1:],y)        
    elif ord(x[0])>96 and ord(x[0])<122:
        letter=(chr(ord(x[0])+1))
        y.append(letter)
        return encrypt(x[1:],y)
    elif ord(x[0])==122:
        letter='a'
        y.append(letter)
        return encrypt(x[1:],y)
# gets input message and outputs encrypted message    
def main():
    Y=[]
    x=input('Enter a message:\n')
    encrypt(x,Y)
    print('Encrypted message:')
    print(''.join(Y))
main()