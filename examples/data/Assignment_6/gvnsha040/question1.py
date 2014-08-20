
z=[]
x=(input('Enter strings (end with DONE):\n'))

    
gal = len(x)
z=[]
if x != 'DONE':
    z.append(x)
while x != 'DONE':
    x=input()
    boy=len(x)
    if boy>gal:
        gal=boy
    
    if x != 'DONE':
        z.append(x)
print()
        
    
    
    
y=(len(z))
s=0
print('Right-aligned list:')
while s < y:
    print(z[s].rjust(gal))
    s+=1
    