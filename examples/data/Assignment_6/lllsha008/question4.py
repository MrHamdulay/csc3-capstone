#Shaylan Lalloo
#counts passes and graphs
print('Enter a space-separated list of marks:')

myin = list(map(int, input().split()))
#reads input

mycounts = [0, 0, 0, 0, 0]
#default counts

for i in myin:
    if i < 50:
        mycounts[4] += 1
    elif (50 <= i < 60):
        mycounts[3] += 1
    elif 60 <= i < 70:
        mycounts[2] += 1
    elif 70 <= i < 75:
        mycounts[1] += 1
    else:
        mycounts[0] += 1
#puts marks in appropriate lists

print('1 |' + 'X' * mycounts[0])
print('2+|' + 'X' * mycounts[1])
print('2-|' + 'X' * mycounts[2])
print('3 |' + 'X' * mycounts[3])
print('F |' + 'X' * mycounts[4])
#outputs each kind of pass plus graphs
