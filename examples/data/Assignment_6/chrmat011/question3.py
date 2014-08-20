print('Independent Electoral Commission')
print('--------------------------------')
print('Enter the names of parties (terminated by DONE):')
votes = {}
inp = ''
while inp != 'DONE':
    inp = input('')
    if inp != 'DONE':
        if inp in list(votes.keys()):
            votes[inp]+=1
        else:
            votes[inp] = 1

x = list(votes.keys())
x = sorted(x)

print('')
print('Vote counts:')

for i in x:
    print('{:<10} -'.format(i),votes[i])
