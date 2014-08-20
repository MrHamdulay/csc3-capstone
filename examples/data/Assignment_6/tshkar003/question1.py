
z=[]
karidas=(input('Enter strings (end with DONE):\n'))

    
gal = len(karidas)
z=[]
if karidas != 'DONE':
    z.append(karidas)
while karidas != 'DONE':
    karidas=input()
    boy=len(karidas)
    if boy>gal:
        gal=boy
    
    if karidas != 'DONE':
        z.append(karidas)
print()
        
    
    
    
y=(len(z))
s=0
print('Right-aligned list:')
while s < y:
    print(z[s].rjust(gal))
    s+=1
    