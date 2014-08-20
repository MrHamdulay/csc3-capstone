marks = input('Enter a space-separated list of marks:\n').split(' ')
for i in range(len(marks)):
    marks[i] = int(marks[i])

cats = [0]*5

for i in marks:
    if i >= 75:
        cats[0] += 1
    elif i >= 70:
        cats[1] += 1
    elif i >= 60:
        cats[2] += 1
    elif i >= 50:
        cats[3] += 1
    else:
        cats[4] += 1

print('1 |' + ('X'*cats[0]))
print('2+|' + ('X'*cats[1]))
print('2-|' + ('X'*cats[2]))
print('3 |' + ('X'*cats[3]))
print('F |' + ('X'*cats[4]))
