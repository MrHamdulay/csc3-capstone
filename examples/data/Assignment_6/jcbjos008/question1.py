'''Joshen Credelio Jacob
Right aligned list of names
21/04/2014'''

names=[]
aname=input('Enter strings (end with DONE):\n')

#adding names to list
while aname!='DONE':
    names.append(aname)
    aname=input('')
    
if len(names) > 0:
    x=len(names[0])

#calculating max length of a name in the list
for i in range (1,len(names),1):
            
    temp = len(names[i])
            
    if (temp > x):
        x = temp

print('\nRight-aligned list:')
for i in range(len(names)):
    
    print(" " * (x - len(names[i])) + names[i])
            
            