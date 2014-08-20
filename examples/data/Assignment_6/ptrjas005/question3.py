'''Jason Pietersen'''
print('Independent Electoral Commission')
print('-'*32)
x=input('Enter the names of parties (terminated by DONE):\n')
partynames=[]
parties={}
form='{0:<10}'
while (x!='DONE'):
    if not x in parties:
        partynames.append(x)
        parties[x]=1
    else:
        parties[x] +=1
    x=input()
partynames.sort()
print()
print('Vote counts:')
for i in partynames:
    print(form.format(i),'-',parties[i])