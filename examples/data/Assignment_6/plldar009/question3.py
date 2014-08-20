print('Independent Electoral Commission')
print('--------------------------------')
x=input('Enter the names of parties (terminated by DONE):\n')

candidates=[]
votes = {}
while x!='DONE':
    candidates.append(x)
    votes[x] = 0
    x=input('')
candidates.sort()
for i in candidates:
    votes[i]+=1
print()
print('Vote counts:')
tmp = []
for i in set(candidates):
    tmp.append(i)
tmp.sort()
for i in tmp:
    print(i + ' ' * (10 - len(i))+' - '+str(votes[i]))