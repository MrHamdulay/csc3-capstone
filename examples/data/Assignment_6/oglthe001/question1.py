"""theresa ogallo 2014
printing out a right-aligned list of strings"""

print('Enter strings (end with DONE):')

# getting a list of strings
x=[]
n=''
while n != 'DONE':
    n=input('')
    x.append(n)


#getting longest string 
y=max(x, key=len)
z=len(y)

#printing out a right-aligned list of strings
print()
x.remove('DONE')
print('Right-aligned list:')
for i in x:
    print (i.rjust(z,))
