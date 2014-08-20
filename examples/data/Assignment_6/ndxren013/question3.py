#Reneshan Naidoo
#counts votes

print('Independent Electoral Commission')
print('--------------------------------')
print('Enter the names of parties (terminated by DONE):')
#basic inputs

votees = []
voted = {}

sent = input()

while sent != 'DONE':
    votees.append(sent)
    sent = input()
#reads votes

for i in votees:
    voted[i] = 0

for i in votees:
    voted[i] += 1
#counts votes

votees.sort()
#sort names

last = ''

print()
print('Vote counts:')

for i in votees:
    if last == i:
        continue
    else:
        print(i + ' ' * (10 - len(i)), '-' ,  voted[i])
        last = i
#output accordingly
