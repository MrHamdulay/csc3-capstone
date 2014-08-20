'''Counting Parties
Limpho Parkies
24-04-2014'''

party_names={}
print('Independent Electoral Commission')
print('--------------------------------')
name=input('Enter the names of parties (terminated by DONE):\n')
while name!='Done' and name!='done' and name!='DONE':
    if name not in party_names:
        party_names[name]= 1
        name=input('')
    else:
        party_names[name] +=1
        name=input('')
print()        
print('Vote counts:')
for name in sorted(party_names):
    r = "{0:<10}".format(name)
    print(r,'-', party_names[name])