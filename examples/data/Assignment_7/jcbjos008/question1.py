'''Joshen Credelio Jacob
30/04/2014
Erasing duplicates'''


#getting a list of strings
x = input('Enter strings (end with DONE):\n')
y=[]
z=[]

#creating a list
while x!='DONE':
    y.append(x)
    x=input('')
    
#deleting duplicates        
for items in y:
    if items not in z:
        z.append(items)
        
#printing list without duplicates
print()
print('Unique list:')
for items in z:
    print(items)
    