marks = input('Enter a space-separated list of marks:\n').split(' ')
counter = [0,0,0,0,0]
for i in range(len(marks)):
    if int(marks[i]) < 50:
        counter[4] += 1
    elif int(marks[i]) < 60:
        counter[3] += 1
    elif int(marks[i]) < 70:
        counter[2] += 1
    elif int(marks[i]) < 75:
        counter[1] += 1
    else:
        counter[0] += 1
display = ['1 |','2+|','2-|','3 |','F |']
for i in range(5):
    print(display[i],'X'*counter[i],sep='')
