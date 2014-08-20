z = input('Enter a message:\n')
def pairing(z):
    
    if len(z)==0 or len(z)==1:  
        return 0
    
    elif z[0]==z[1]:
        return 1 + pairing(z[2:])  
    
    elif z[0]!=z[1]:
        return pairing(z[1:])
    
print('Number of pairs:',pairing(z))
    