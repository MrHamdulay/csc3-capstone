#kairav soni
x=(input('Enter strings (end with DONE):\n'))

print("")    
widthx=len(x)
z=[]

if x!="DONE":
    z.append(x)
    
while x!="DONE":
    x=input()
    widthxn=len(x)
    
    if widthxn>widthx:
        widthx=widthxn
    
    if x!="DONE":
        z.append(x)
        
    
    
    
form=(len(z))

search=0

print('Right-aligned list:')

while search < form:
    print(z[search].rjust(widthx))
    search=search+1
    