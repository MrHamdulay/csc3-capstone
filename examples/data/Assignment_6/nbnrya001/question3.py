

print('Independent Electoral Commission')
print('--------------------------------')
print('Enter the names of parties (terminated by DONE):')

votes = []

cur = input()

while cur != 'DONE':
    votes.append(cur)
    cur = input()

print()
print('Vote counts:')

votes.sort()

count = 0
for i in range(len(votes)):
    if i == len(votes) - 1 or votes[i] != votes[i + 1]:
        print('{0:<10}'.format(votes[i]), '-', count + 1)
        count = 0
    else:
        count += 1

