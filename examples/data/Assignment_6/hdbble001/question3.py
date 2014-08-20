print('Independent Electoral Commission\n--------------------------------')
name=input('Enter the names of parties (terminated by DONE):\n')

parties=[]

while not name=='DONE':
    parties.append(name)
    name=input()
    if name=="DONE":
        break


print()
print("Vote counts:")

parties.sort()
seen=[]
for name in parties:
    if not name in seen:
        print ("{0:10}{1}{2}".format(name, " - ", parties.count(name)))
        seen.append(name)