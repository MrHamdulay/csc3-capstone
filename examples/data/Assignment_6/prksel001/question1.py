'''Right aligning of strings
Limpho Parkies
24-04-2014'''

#function for asking the names
list_names=[]
name=input('Enter strings (end with DONE):\n')
while name!='DONE' and name!='Done':
        list_names.append(name)
        name=input('')
#longest word
print()
print('Right-aligned list:')
maxim=0
for i in list_names:
    if len(i)>maxim:
        maxim=len(i)
#aligning
for j in list_names:
    r = ("{0:>" + str(maxim)  + "}").format(j)
    print(r)

