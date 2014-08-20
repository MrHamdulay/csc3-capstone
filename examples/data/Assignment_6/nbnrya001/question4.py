
marks = ['1 |', '2+|', '2-|', '3 |', 'F |']

room = list(map(lambda x: int(x), input('Enter a space-separated list of marks:\n').split()))

for i in room:
    if i < 50:
        marks[4] += 'X'
    elif 50 <= i < 60:
        marks[3] += 'X'
    elif 60 <= i < 70:
        marks[2] += 'X'
    elif 70 <= i < 75:
        marks[1] += 'X'
    else:
        marks[0] += 'X'

fuck = lambda x : print(x)

for i in marks:
    fuck(i)
