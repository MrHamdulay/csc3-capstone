''' Program that prints histogram representation of marks according to the mark categories at UCT 
Othniel KONAN
KNNOTH001
2014/04/19'''

#CREATION OF BASE OF THE HISTOGRAM
array=[['1',' ','|'],['2','+','|'],['2','-','|'],['3',' ','|'],['F',' ','|']]

#INPUT THE LIST
lt = input('Enter a space-separated list of marks:\n')
lt = lt.split(' ')

#ADD 'X' ACCORDING TO THE MARK ALLOCATION
for mark in lt:
    if 0 <= int(mark) < 50:
        array[4].append('X')
    elif 50 <= int(mark) < 60:
        array[3].append('X')
    elif 60 <= int(mark) < 70:
        array[2].append('X')
    elif 70 <= int(mark) < 75:
        array[1].append('X')
    elif 75 <= int(mark) <= 100:
        array[0].append('X')

#PRINT THE ARRAY
for x in range(len(array)):
    for y in range(len(array[x])):
        print(array[x][y],end='')
    print()

    
    